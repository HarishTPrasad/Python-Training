# develop a function to add remove and display task in a to do list
import os

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "todolist.txt"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks in the to-do list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")
        self.save_tasks()

    def complete_task(self, index):
        if 1 <= index <= len(self.tasks):
            completed_task = self.tasks.pop(index - 1)
            print(f"Task '{completed_task}' marked as complete.")
            self.save_tasks()
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Task '{deleted_task}' deleted from the to-do list.")
            self.save_tasks()
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as complete: "))
            todo_list.complete_task(index)
        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            print("Exiting the todo list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

