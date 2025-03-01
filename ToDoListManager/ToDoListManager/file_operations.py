import os
from pathlib import Path


def load_user_name() -> str:
    """
    Loads the user's name from 'names.txt'. If not found, prompts the user and saves it.
    """
    file_path = Path("names.txt")

    if file_path.exists():
        with open(file_path, "r") as file:
            user_name = file.readline().strip()
            return user_name

    user_name = input("Enter your name: ").strip()
    with open(file_path, "w") as file:
        file.write(user_name)

    return user_name


# def save_tasks(task_manager) -> None:
#     """
#     Saves active, completed, and deleted tasks to respective files.
#     """
#     with open("Active.txt", "w") as active_file:
#         for task in task_manager.active_tasks:
#             active_file.write(str(task) + "\n")
#
#     with open("Completed.txt", "w") as completed_file:
#         for task in task_manager.completed_tasks:
#             completed_file.write(str(task) + "\n")
#
#     with open("Deleted.txt", "w") as deleted_file:
#         for task in task_manager.deleted_tasks:
#             deleted_file.write(str(task) + "\n")

import os
import json
from typing import List, Dict


def load_tasks(file_name: str) -> List[Dict]:
    """
    Loads tasks from a specified file. If the file does not exist, an empty list is returned.

    :param file_name: Name of the file to load tasks from.
    :return: A list of tasks loaded from the file.
    """
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            try:
                tasks = json.load(file)  # Load JSON data
                return tasks if isinstance(tasks, list) else []
            except json.JSONDecodeError:
                print(f"Warning: {file_name} is empty or corrupted. Creating a new task list.")
                return []
    return []


def save_tasks(active_tasks: List[Dict], completed_tasks: List[Dict], deleted_tasks: List[Dict]) -> None:
    """
    Saves active, completed, and deleted tasks to their respective files.

    :param active_tasks: List of active tasks.
    :param completed_tasks: List of completed tasks.
    :param deleted_tasks: List of deleted tasks.
    """
    with open("Active.txt", "w", encoding="utf-8") as active_file:
        json.dump(active_tasks, active_file, indent=4)

    with open("Completed.txt", "w", encoding="utf-8") as completed_file:
        json.dump(completed_tasks, completed_file, indent=4)

    with open("Deleted.txt", "w", encoding="utf-8") as deleted_file:
        json.dump(deleted_tasks, deleted_file, indent=4)
