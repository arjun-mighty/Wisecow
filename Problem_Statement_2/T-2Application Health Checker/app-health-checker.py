# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///

"""
Script to check if an application is up or down using http status codes.
This script uses custom http codes.
Below are the custom http code used
- 999 : for connection errors
- 998 : for connection timeout errors
- 997 : for cases where connection established but 
        server didn't response with in time
"""
import requests
from requests.exceptions import ConnectionError, ConnectTimeout, ReadTimeout
import time



def make_get(base_url, timeout=60) -> int:
    try:
        response = requests.get(base_url, timeout=timeout)
        return response.status_code
    except ReadTimeout:
        return 997
    except ConnectTimeout:
        return 998
    except ConnectionError:
        return 999
    
def make_post(base_url, data, timeout=60) -> int:
    try:
        response = requests.post(base_url, json=data, timeout=timeout)
        return response.status_code
    except ReadTimeout:
        return 997
    except ConnectTimeout:
        return 998
    except ConnectionError:
        return 999

def main() -> None:
    url = "http://localhost:8000/"
    interval = 4

    while True:
        response_codes = []
        response_codes.append(make_get(url))
        response_codes.append(make_post(url, {"name": "Arjun"}))

        for code in response_codes:
            if code >= 500:
                print("Application is Down.")
                break
        else:
            print("Application is Up.")

        time.sleep(interval)


if __name__ == "__main__":
    main()
