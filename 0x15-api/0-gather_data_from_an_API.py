#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,"""
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    direct = "/todos"
    us = "/users"
    cod = "?userId={}".format(int(sys.argv[1]))
    web_all = requests.get(url + direct + cod).json()
    web_user = requests.get(url + us + "/" + sys.argv[1]).json()

    data_title = []

    for task in web_all:
        if (task.get('completed') is True):
            data_title.append(task.get('title'))

    num_tasks = len(data_title)
    num_total = len(web_all)

    print("Employee {} is done with tasks({}/{}):".format(web_user.get('name'),
          num_tasks, num_total))

    for row in data_title:
        print("\t {}".format(row))
