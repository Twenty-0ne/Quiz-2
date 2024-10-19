# task_manager.py
from task import Task

class TaskManager:
    # Manages the task list and CRUD operations.
    
    def __init__(self):
        # Initializes an empty task list.
        self.tasks = []

    def create_task(self, name, description, due_date, priority):
        # Creates and adds a new task.
        new_task = Task(name, description, due_date, priority)
        self.tasks.append(new_task)
        print(f"Task '{name}' created.")

    def display_tasks(self):
        # Shows all tasks.
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"Task {idx}:\n{task}")

    def update_task(self, index, name=None, description=None, due_date=None, priority=None):
        # Updates an existing task.
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.name = name or task.name
            task.description = description or task.description
            task.due_date = due_date or task.due_date
            task.priority = priority or task.priority
            print(f"Task {index + 1} updated.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        # Removes a task from the list.
        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks.pop(index)
            print(f"Task '{deleted_task.name}' deleted.")
        else:
            print("Invalid task index.")