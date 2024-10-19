# main.py
from task_manager import TaskManager  # Import the TaskManager class to manage tasks

def main():
    task_manager = TaskManager()  # Create an instance of TaskManager
    
    while True:
        # Display the main menu options
        print("\nTask Manager")
        print("1. Create a new task")
        print("2. View tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Get user choice

        if choice == "1":
            # Create a new task
            name = input("Enter task name: ")  # Get task name
            description = input("Enter task description: ")  # Get task description
            due_date = input("Enter task due date (YYYY-MM-DD): ")  # Get task due date
            priority = input("Enter task priority (Low, Medium, High): ")  # Get task priority
            task_manager.create_task(name, description, due_date, priority)  # Create the task

        elif choice == "2":
            # Display all tasks
            task_manager.display_tasks()  # Call the display method to show tasks

        elif choice == "3":
            # Update an existing task
            task_manager.display_tasks()  # Show current tasks
            index = int(input("Enter the task number to update: ")) - 1  # Get the task index to update
            name = input("Enter new name (leave blank to keep current): ")  # Get new name or keep current
            description = input("Enter new description (leave blank to keep current): ")  # Get new description
            due_date = input("Enter new due date (leave blank to keep current): ")  # Get new due date
            priority = input("Enter new priority (leave blank to keep current): ")  # Get new priority
            task_manager.update_task(index, name, description, due_date, priority)  # Update the task

        elif choice == "4":
            # Delete a task
            task_manager.display_tasks()  # Show current tasks
            index = int(input("Enter the task number to delete: ")) - 1  # Get the task index to delete
            task_manager.delete_task(index)  # Delete the task

        elif choice == "5":
            # Exit the program
            print("Exiting Task Manager...")  # Notify user of exit
            break  # Exit the loop

        else:
            print("Invalid choice.")  # Handle invalid choice

if __name__ == "__main__":
    main()  # Run the main function