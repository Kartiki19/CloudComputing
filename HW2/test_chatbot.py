import time
import requests
# Invoke chatbot handler and calculate total execution time
def invoke_chatbot(query):
    start_time = time.time()
    response = requests.post("http://192.168.64.6:8080/function/chatbot", data=query)
    execution_time = time.time() - start_time
    #print("Response:", response.text)
    print("Execution Time: " + str(execution_time) + "sec.\n")
    return response, execution_time

## a-b No figlet calls
queries = ["What is your name ?", "What is the current time ?"]
testcases = ["a. First request that does not call figlet: ", "b. Second request that does not call figlet"]
for testcase in range(2):
    print("\n***** " + testcases[testcase] + " *****")
    invoke_chatbot(queries[testcase])

#c. Average over 10 requests that does not call figlet
total_execution_time = 0
print("\n******* c. Average over 10 requests that does not call figlet: *******")
for request in range(10):
    query = "What is your name?"
    response, execution_time = invoke_chatbot(query)
    total_execution_time += execution_time
average_execution_time = total_execution_time / 10
print("Average Execution Time: " + str(average_execution_time) + " sec.")

## d-e Figlet Calls
queries = ["figlet for Hello World", "figlet for Hello COEN"]
testcases = ["d. First request that calls figlet", "e. Second request that calls figlet"]
for testcase in range(2):
    print("\n******* " + testcases[testcase] + " *******")
    invoke_chatbot(queries[testcase])

# f. Second request that calls figlet that follows the first request that does not call figlet
print("******* F. Second request that calls figlet that follows the first request that does not call figlet ******")
queries = ["What is todays date ?", "figlet for Hello Kartiki"]
testcases = ["[f1]. First request that does not calls figlet", "[12]. Second request that calls figlet"]
for testcase in range(2):
    print("\n******* " + testcases[testcase] + " *******")
    invoke_chatbot(queries[testcase])

#g. Average over 10 requests that do call figlet
total_execution_time = 0
print("\n******* g. Average over 10 requests that do call figlet: *******")
for request in range(10):
    query = "figlet for Hello World"
    response, execution_time = invoke_chatbot(query)
    total_execution_time += execution_time 
average_execution_time = total_execution_time / 10
print("Average Execution Time: " + str(average_execution_time) + " sec.")