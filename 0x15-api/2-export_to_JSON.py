#!/usr/bin/python3
"""Exports fetched data from an API to JSON file"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[2]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"user_id": user_id}.json())

    with open("{}.json".format(user_id), "w") as jsonfile:
        writer = json.dump(
            {user_id : [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": todo.get("username")
        } for todo in todos]}, jsonfile)
