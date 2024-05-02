#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(
        URL + "users/{}".format(sys.argv[1]), timeout=10).json()
    todos = requests.get(
        URL + "todos", params={"userId": sys.argv[1]}, timeout=10).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for c in completed:
        print("\t {}".format(c))
