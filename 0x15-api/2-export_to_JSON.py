#!/usr/bin/python3
"""the task #0, extend your Python script to export data in the CSV format."""
import json
import requests
import sys


if __name__ == "__main__":

    arg = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"
    direct = "/todos"
    us = "/users"
    cod = "?userId={}".format(arg)
    web_all = requests.get(url + direct + cod).json()
    web_user = requests.get(url + us + "/{}".format(arg)).json()

    data_title = [{"task": task.get('title'),
                   "completed": task.get('completed'),
                   "username": web_user.get('username')} for task in web_all]

    file_json = "{}.json".format(arg)

    with open(file_json, 'w', newline='') as json_file:
        json.dump({arg: data_title}, json_file)
