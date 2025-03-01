from file_operations import load_tasks, save_tasks
from add_task import add_task
from delete_task import delete_task
from edit_task import edit_task_name
from view_task import view_tasks
from mark_complete import mark_task_as_complete


class TaskManager:
    def __init__(self):
        """
        Initializes the TaskManager and loads existing tasks from files.
        If files don't exist, initializes empty task lists.
        """
        self.active_tasks = load_tasks("Active.txt")
        self.completed_tasks = load_tasks("Completed.txt")
        self.deleted_tasks = load_tasks("Deleted.txt")

    def add_task(self) -> None:
        """Adds a new task and saves changes."""
        self.active_tasks = add_task(self.active_tasks)
        self._save_all_tasks()

    def view_active_tasks(self) -> None:
        """Displays active tasks."""
        view_tasks(self.active_tasks, "Active Tasks")

    def view_completed_tasks(self) -> None:
        """Displays completed tasks."""
        view_tasks(self.completed_tasks, "Completed Tasks")

    def view_deleted_tasks(self) -> None:
        """Displays deleted tasks."""
        view_tasks(self.deleted_tasks, "Deleted Tasks")

    def edit_task_name(self) -> None:
        """Edits an active task name and saves changes."""
        self.active_tasks = edit_task_name(self.active_tasks)
        self._save_all_tasks()

    def mark_task_as_complete(self) -> None:
        """Marks an active task as complete and saves changes."""
        self.active_tasks, self.completed_tasks = mark_task_as_complete(self.active_tasks, self.completed_tasks)
        self._save_all_tasks()

    def delete_task(self) -> None:
        """Deletes an active task and saves changes."""
        self.active_tasks, self.deleted_tasks = delete_task(self.active_tasks, self.deleted_tasks)
        self._save_all_tasks()

    def _save_all_tasks(self) -> None:
        """Saves all tasks to their respective files."""
        save_tasks(self.active_tasks, self.completed_tasks, self.deleted_tasks)
