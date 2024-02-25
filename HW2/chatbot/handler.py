import requests
import datetime
import re
import random

# Generate figlet for input
def generate_figlet(input):
    figletResponse = requests.post("http://192.168.64.6:8080/function/figlet", data=input)
    if figletResponse.status_code == 200:
        response = figletResponse.text
    else:
        response = "ERROR: Failed to perform the operation. Status Code: " + str(figletResponse.status_code) + ", Error Message: "  + str(figletResponse.text)
    return response

def handle(req):
    # Convert the input string to lowercase for case-insensitive matching
    query = req.lower()

    if 'figlet for name' in query:
        response = generate_figlet("ChatBot")
    elif 'figlet for date' in query:
        current_date = datetime.datetime.now().date()
        response = generate_figlet(str(current_date))
    elif 'figlet for time' in query:
        current_time = datetime.datetime.now().time()
        return generate_figlet(str(current_time))
    elif 'name' in query:
        response = random.choice(["Hello, my name is ChatBot", 
                              "You can call me ChatBot", 
                              "Hello, I am ChatBot"])
    elif 'date' in query:
        current_date = datetime.datetime.now().date()
        response = random.choice(["Current date is: " + str(current_date),
                              "Today's date is: " + str(current_date),
                              "At this moment the date reads as " + str(current_date)])
    elif 'time' in query:
        current_time = datetime.datetime.now().time()
        response = random.choice(["Time is: " + str(current_time),
                              "Rightnow the clock shows " + str(current_time),
                              "Current time is: " + str(current_time)])
    elif 'figlet' in query:
        pattern = r"figlet for (.*)"
        match = re.search(pattern, query)
        if match:
            response = generate_figlet(match.group(1))
        else:
            response = "Write figlet query in format : figlet for <text>"
    else:
        response = """ I apologize, I did not understand your question. 
                        Please try again with following questions :
                        1. What is your name ?
                        2. What is current time ?
                        3. Generate figlet for <text> """

    return response