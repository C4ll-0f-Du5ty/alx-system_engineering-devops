#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""
import json
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

    file = f"{employee_ID}.json"
    with open(file, mode='w', newline='', encoding='utf-8') as f:
        json.dump({employee_ID: [{
            "task": r.get("title"),
            "completed": r.get("completed"),
            "username": r1.get("username")} for r in r2]}, f)
