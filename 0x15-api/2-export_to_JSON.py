#!/usr/bin/python3

"""
This module provides a function to export user tasks to a JSON file.
"""

import sys
import utils_methods

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <user_id>\n")
        sys.exit(1)

    user_id = sys.argv[1]
    user = utils_methods.get_username(user_id)
    if user is None:
        sys.stderr.write("Invalid user id.\n")
        sys.exit(1)

    todos = utils_methods.get_todos(user_id)
    utils_methods.export_to_json(user_id=user_id, username=user, tasks=todos)
