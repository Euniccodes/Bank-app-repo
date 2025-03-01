def delete_task(active_tasks: list[dict], deleted_tasks: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Deletes a task by changing its status to 'Deleted' and moving it to the deleted tasks list.

    :param active_tasks: List of active tasks
    :param deleted_tasks: List of deleted tasks
    :return: Updated active and deleted tasks lists
    """
    if not active_tasks:
        print("No active tasks available to delete.")
        return active_tasks, deleted_tasks

    for task in active_tasks:
        print(f"ID: {task['task_id']} | Name: {task['task_name']}")

    try:
        task_id = int(input("Enter task ID to delete: ").strip())
        for task in active_tasks:
            if task["task_id"] == task_id:
                task["task_status"] = "Deleted"
                deleted_tasks.append(task)
                active_tasks.remove(task)
                print(f"Task {task_id} deleted successfully.")
                return active_tasks, deleted_tasks
        print("Invalid Task ID!")
    except ValueError:
        print("Invalid input! Please enter a valid Task ID.")

    return active_tasks, deleted_tasks
