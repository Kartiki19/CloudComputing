#!/bin/bash

# Calculate Events/Sec
cal_events_per_sec() {
	local events=$1
	local total_time=$2
	local events_per_sec=$(bc <<< "scale=4; $events / $total_time")
	echo $events_per_sec
}
run_sysbench_fileio(){
	local parameter_val=$1
	local readings

	echo "Parameter Value = $parameter_val"

	sysbench --test=fileio --file-total-size=2G --file-test-mode=$parameter_val prepare
	result=$(sysbench --test=fileio --file-total-size=2G --file-test-mode=$parameter_val run)
	echo "result : $result"
	sysbench --test=fileio --file-total-size=2G --file-test-mode=$parameter_val cleanup


	total_time=$(echo "$result" | grep -oP "total time:\s+\K(\d+\.\d+)")
	total_events=$(echo "$result" | grep -oP "total number of events:\s+\K(\d+)")
	events_per_sec=$(cal_events_per_sec $total_events $total_time)

	echo "Total Time = $total_time , Total Events = $total_events, Event/Sec = $events_per_sec"

	# Save in .csv
	readings+=$(echo ",$total_time,$total_events,$events_per_sec")
	echo "fileio,$parameter_val,$readings" >> sysbench_readings_fileio.csv
}

# Main Function
# Creating a .csv file with header
#echo "Test Mode,Parameter Value,Total Time(sec),Number of Events,Events/Sec" > sysbench_readings_fileio.csv

# SysBench Test Mode = FileIo
run_sysbench_fileio "$1"
