#!/bin/bash

# Calculate Events/Sec
cal_events_per_sec() {
	local events=$1
	local total_time=$2
	local events_per_sec=$(bc <<< "scale=4; $events / $total_time")
	echo $events_per_sec
}

# Run Sysbench test and save results in .csv file
run_sysbench_test(){
	local test_mode=$1
	local parameter_val=$2
	local readings

	echo "Test Mode = $test_mode, Parmeter = $parameter_val"

	for i in {1..5}; do
		echo "Run : $i"

		result=$(sysbench --test=$test_mode $parameter_val run | grep -E "total time:|total number of events:")
		total_time=$(echo "$result" | grep -oP "total time:\s+\K(\d+\.\d+)")
		total_events=$(echo "$result" | grep -oP "total number of events:\s+\K(\d+)")
		events_per_sec=$(cal_events_per_sec $total_events $total_time)

		echo "Total Time = $total_time, Total Events = $total_events, Events/Sec = $events_per_sec"

		# Save in .csv
		readings+=$(echo ",$total_time,$total_events,$events_per_sec")
	done

	param_val=$(echo $parameter_val | grep -oP '\d+G|\d+')
	echo "$test_mode,$param_val,$readings" >> sysbench_readings.csv
}

# Main Function
# Creating .csv file with headers
echo "Test Mode,Parameter Value,Total Time(sec),Number of Events,Events/Sec" > sysbench_readings.csv

# SysBench Test Mode = cpu
run_sysbench_test cpu "--cpu-max-prime=30000"
run_sysbench_test cpu "--cpu-max-prime=60000"

# SysBench Test Mode = memory
run_sysbench_test memory "--memory-block-size=1G"
run_sysbench_test memory "--memory-block-size=2G"


