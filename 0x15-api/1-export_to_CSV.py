#!/usr/bin/python3
"""Exports todo list info for an employee id to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[2]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"user_id": user_id}.json())

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, todo.get("completed"), todo.get("title")])
         for todo in todos]
