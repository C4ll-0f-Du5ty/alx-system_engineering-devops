#!/usr/bin/python3
import requests
import sys


url = "https://jsonplaceholder.typicode.com/"
employee_ID = sys.argv[1]
response1 = requests.get(url + "users/" + employee_ID)
r1 = response1.json()

params = {"userId": employee_ID}

response2 = requests.get(url + "/todos", params)
r2 = response2.json()

completed = []

for t in r2:
    if t['completed'] is True:
        completed.append(t['title'])

print(f"Employee {r1['name']} is done with tasks({len(completed)}/{len(r2)}):")

for t in completed:
    print(f'\t {t}')
