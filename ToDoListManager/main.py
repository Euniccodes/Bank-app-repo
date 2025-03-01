from menu import display_menu
from file_operations import load_user_name, save_tasks
from task_manager import TaskManager


def main() -> None:
    """
    Entry point of the Todo List Manager application.
    Manages user interactions and performs requested actions.
    """
    user_name = load_user_name()
    print(f"Hello {user_name}, this is your Todo List Manager 👋. How may I help you today?\n")

    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_active_tasks()
        elif choice == "3":
            task_manager.view_completed_tasks()
        elif choice == "4":
            task_manager.view_deleted_tasks()
        elif choice == "5":
            task_manager.edit_task_name()
        elif choice == "6":
            task_manager.mark_task_as_complete()
        elif choice == "7":
            task_manager.delete_task()
        elif choice == "8":
            save_tasks(task_manager)
            print("Exiting the program. Your tasks have been saved. Goodbye!")
            break
        else:
            print("Invalid option! Please enter a number between 1 and 8.\n")


if __name__ == "__main__":
    main()
