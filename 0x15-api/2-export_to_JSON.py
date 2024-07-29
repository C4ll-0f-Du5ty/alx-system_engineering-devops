#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_ID = sys.argv[1]
    response1 = requests.get(url + "users/" + employee_ID)
    r1 = response1.json()

    params = {"userId": employee_ID}
    response2 = requests.get(url + "/todos", params=params)
    r2 = response2.json()

    file = f"{employee_ID}.json"
    Data = ['{"task": "{}", "completed": {}, "username": "{}"'.
            format(r.get("title"), r.get("completed"), r1.get("username")) for r in r2]
    D = ',\n'.join(Data)  # Join items with a comma and newline for readability
    with open(file, mode='w', encoding='utf-8') as f:
        f.write('[\n')
        f.write(D)
        f.write('\n]')
