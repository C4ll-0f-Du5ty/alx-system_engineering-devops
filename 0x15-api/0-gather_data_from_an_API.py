#!/usr/bin/python3 
import requests
import sys


employee_ID = sys.argv[1]
response1 = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_ID}')
r1 = response1.json()

params = {"userId": employee_ID}

response2 = requests.get(f"https://jsonplaceholder.typicode.com/todos", params)
r2 = response2.json()

completed = []

for t in r2:
    if t['completed'] == True:
        completed.append(t['title'])

print(f"Employee {r1['name']} is done with tasks({len(completed)}/{len(r2)}):")

for t in completed:
    print(f'\t {t}')
