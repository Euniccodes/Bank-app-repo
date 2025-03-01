def edit_task_name(active_tasks: list[dict]) -> list[dict]:
    """
    Allows the user to edit the name of an active task.

    :param active_tasks: List of active tasks
    :return: Updated list of active tasks
    """
    if not active_tasks:
        print("No active tasks available to edit.")
        return active_tasks

    for task in active_tasks:
        print(f"ID: {task['task_id']} | Name: {task['task_name']}")

    try:
        task_id = int(input("Enter task ID to edit: ").strip())
        for task in active_tasks:
            if task["task_id"] == task_id:
                new_name = input("Enter new task name: ").strip()
                task["task_name"] = new_name
                print(f"Task {task_id} name updated to '{new_name}'.")
                return active_tasks
        print("Invalid Task ID!")
    except ValueError:
        print("Invalid input! Please enter a valid Task ID.")

    return active_tasks
