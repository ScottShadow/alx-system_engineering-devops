#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import sys
import requests


if __name__ == "__main__":
    user_id = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + "users/{}".format(user_id), timeout=10).json()
    username = user.get("username")
    todos = requests.get(
        URL + "todos", params={"userId": user_id}, timeout=10).json()

    with open("{}.csv".format(user_id), "w", newline="",
              encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                [user_id, username, t.get("completed"), t.get("title")])
