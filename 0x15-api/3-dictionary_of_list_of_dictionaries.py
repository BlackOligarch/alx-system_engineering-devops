#!/usr/bin/python3

"""
This module provides a function to export all tasks to a JSON file.
"""

import utils_methods


if __name__ == "__main__":
    # get user info and todos once so we can minimize the number of requests.
    # this helps to achieve more speed since everything will be done locally
    # after the data has been retrieved.
    users = utils_methods.get_users()
    todos = utils_methods.get_todos()
    utils_methods.export_all_to_json(users=users, tasks=todos)
