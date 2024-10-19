# task.py

class Task:
    # Represents a task with name, description, due date, and priority.
    
    def __init__(self, name, description, due_date, priority):
        # Initializes the task with the provided attributes.
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        # Returns a string representation of the task.
        return f"Task Name: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\n"