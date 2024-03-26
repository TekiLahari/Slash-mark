# Define an empty list to store tasks
user_tasks = []

# Function to display the to-do list
def show_tasks():
    if not user_tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, user_task in enumerate(user_tasks, start=1):
            task_status = "Done" if user_task["completed"] else "Not Done"
            print(f"{i}. {user_task['task']} ({task_status})")

# Function to add a task to the to-do list
def add_task(task_name):
    task = {"task": task_name, "completed": False}
    user_tasks.append(task)
    print(f"Task '{task_name}' added to your to-do list.")

# Function to mark a task as completed
def complete_task(task_number):
    if 1 <= task_number <= len(user_tasks):
        user_tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task(task_number):
    if 1 <= task_number <= len(user_tasks):
        removed_task = user_tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    user_choice = input("Enter your choice: ")

    if user_choice == '1':
        show_tasks()
    elif user_choice == '2':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif user_choice == '3':
        show_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        complete_task(task_number)
    elif user_choice == '4':
        show_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif user_choice == '5':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
