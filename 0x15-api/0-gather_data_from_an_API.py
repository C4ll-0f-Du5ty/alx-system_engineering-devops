#!/usr/bin/python3
import requests
import sys
"""Gathering Some information and Presenting them in specific foramt"""

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    employee_ID = sys.argv[1]
    response1 = requests.get(url + "users/" + employee_ID)
    r1 = response1.json()

    params = {"userId": employee_ID}

    response2 = requests.get(url + "/todos", params)
    r2 = response2.json()

    completed = []

    for t in r2:
        if t.get('completed') is True:
            completed.append(t['title'])

    print("Employee {} is done with tasks({}/{}):"
          .format(r1.get('name'), len(completed), len(r2)))

    for t in completed:
        print(f'\t {t}')
