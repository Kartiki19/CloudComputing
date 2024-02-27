import requests
import threading
import time

def send_async_request(query):
    url = "http://192.168.64.8:8080/async-function/figlet"
    try:
        response = requests.post(url, query)
        #print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")

def send_requests_parallely():
    threads = []
    for i in range(20000):
        query = "name"
        thread = threading.Thread(target=send_async_request, args=(query,))
        threads.append(thread)
        thread.start()
    # Wait for all threads to finish
    for thread in threads:
        thread.join()


print("erwfhufreju")
start_time = time.time()
send_requests_parallely()
end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
