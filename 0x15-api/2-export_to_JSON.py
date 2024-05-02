#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import sys
import requests

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(
        URL + "users/{}".format(sys.argv[1]), timeout=10).json()
    todos = requests.get(
        URL + "todos", params={"userId": sys.argv[1]}, timeout=10).json()

    with open("{}.json".format(sys.argv[1]), "w",
              encoding="utf-8") as jsonfile:
        json.dump({sys.argv[1]: [
            {"task": t.get("title"), "completed": t.get("completed"),
             "username": user.get("username")}
            for t in todos]}, jsonfile)

    jsonfile.close()
