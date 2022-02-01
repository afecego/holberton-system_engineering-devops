#!/usr/bin/python3
"""the task #0, extend your Python script to export data in the CSV format."""
import csv
import sys
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    direct = "/todos"
    us = "/users"
    cod = "?userId={}".format(int(sys.argv[1]))
    web_all = requests.get(url + direct + cod).json()
    web_user = requests.get(url + us + "/" + sys.argv[1]).json()

    data_title = []

    for task in web_all:
        data_title.append([sys.argv[1], web_user.get("username"),
                          task.get("completed"), task.get("title")])

    file_cvs = sys.argv[1] + ".cvs"

    with open(file_cvs, mode='w', newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        writer.writerows(data_title)
