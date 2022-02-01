#!/usr/bin/python3
"""the task #0, extend your Python script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    direct = "/todos"
    us = "/users"
    web_all = requests.get(url + direct).json()
    web_user = requests.get(url + us).json()

    dic_new = {}

    for user in web_user:
        u_id = user.get('id')
        list_data = [{"username": user.get('username'),
                      "task": task.get('title'),
                      "completed": task.get('completed')
                      } for task in web_all if u_id == task.get('userId')]
        dic_new[u_id] = list_data

    file_json = "todo_all_employees.json"

    with open(file_json, 'w', newline='') as json_file:
        json.dump(dic_new, json_file)
