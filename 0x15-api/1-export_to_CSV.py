#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format."""
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    employee_ID = sys.argv[1]
    response1 = requests.get(url + "users/" + employee_ID)
    r1 = response1.json()

    params = {"userId": employee_ID}

    response2 = requests.get(url + "/todos", params)
    r2 = response2.json()

    file = f"{employee_ID}.csv"
    with open(file, mode='w', newline='', encoding='utf-8') as f:
        for r in r2:
            f.write('"{}","{}","{}","{}"\n'
                    .format(employee_ID,
                            r1.get("username"),
                            r.get("completed"),
                            r.get("title")))
