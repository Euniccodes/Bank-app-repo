def view_tasks(task_list: list[dict], title: str) -> None:
    """
    Prints tasks in a formatted way.

    :param task_list: List of tasks to display
    :param title: Title of the task category
    """
    if not task_list:
        print(f"\n===== {title} =====\nNo tasks available.\n")
        return

    print(f"\n===== {title} =====")
    for task in task_list:
        print(
            f"ID: {task['task_id']}, Name: {task['task_name']}, "
            f"Status: {task['task_status']}, Created: {task['time_created']}, "
            f"Finished: {task['time_finished']}"
        )
    print("========================\n")
