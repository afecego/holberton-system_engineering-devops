#!/usr/bin/python3
"""the task #0, extend your Python script to export data in the CSV format."""
import csv
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

    data_title = []

    for task in web_all:
        data_title.append([arg, web_user.get("username"),
                          task.get("completed"), task.get("title")])

    file_cvs = "{}.cvs".format(arg)

    with open(file_cvs, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        writer.writerows(data_title)
