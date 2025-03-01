from datetime import datetime


def mark_task_as_complete(active_tasks: list[dict], completed_tasks: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Marks an active task as completed and moves it to the completed tasks list.

    :param active_tasks: List of active tasks
    :param completed_tasks: List of completed tasks
    :return: Updated active and completed tasks lists
    """
    if not active_tasks:
        print("No active tasks available to complete.")
        return active_tasks, completed_tasks

    for task in active_tasks:
        print(f"ID: {task['task_id']} | Name: {task['task_name']}")

    try:
        task_id = int(input("Enter task ID to mark as complete: ").strip())
        for task in active_tasks:
            if task["task_id"] == task_id:
                task["task_status"] = "Completed"
                task["time_finished"] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                completed_tasks.append(task)
                active_tasks.remove(task)
                print(f"Task {task_id} marked as completed.")
                return active_tasks, completed_tasks
        print("Invalid Task ID!")
    except ValueError:
        print("Invalid input! Please enter a valid Task ID.")

    return active_tasks, completed_tasks
