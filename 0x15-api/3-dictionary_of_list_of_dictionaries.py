#!/usr/bin/python3
"""Records all tasks from all employees"""
import json
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + "users", timeout=10).json()

    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user.get("username")
            }for t in requests.get(URL + "todos",
                                   params={"userId": user.get("id")},
                                   timeout=10).json()]
            for user in user}, jsonfile)

    jsonfile.close()
