from datetime import datetime


def add_task(active_tasks: list[dict]) -> list[dict]:
    """
    Adds a new task to the active tasks list.

    :param active_tasks: List of active tasks
    :return: Updated list of active tasks
    """
    task_name = input("Enter task name: ").strip()
    task_id = len(active_tasks) + 1

    task = {
        "task_id": task_id,
        "task_name": task_name,
        "task_status": "Active",
        "time_created": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        "time_finished": None
    }

    active_tasks.append(task)
    print(f"Task '{task_name}' added successfully!")
    return active_tasks
