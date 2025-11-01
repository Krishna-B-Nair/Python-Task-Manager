import json # We use json to easily save/load our list of tasks

TASKS_FILE = "tasks.txt"

# --- STEP 2: SAVING AND LOADING ---

def load_tasks():
    """
    Loads the task list from the tasks.txt file.
    If the file doesn't exist, it returns an empty list.
    """
    try:
        # 'with' automatically closes the file for us
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file) # Read the file and turn json string into a list
            return tasks
    except FileNotFoundError:
        # This is not an error! It just means it's the first time running.
        return []

def save_tasks(tasks):
    """
    Saves the current task list to the tasks.txt file.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4) # 'indent=4' makes the file readable
    print("Tasks saved successfully!")

# --- STEP 3: THE "FEATURES" ---

def add_task(tasks):
    """Asks the user for a task and priority, adds it to the list."""
    title = input("Enter the task title: ")
    priority = input("Enter priority (High, Medium, Low): ")
    
    # A task is just a Python dictionary
    task = {
        "title": title,
        "priority": priority,
        "status": "Pending"
    }
    
    tasks.append(task)
    print(f"Task '{title}' added.")

def view_tasks(tasks):
    """Displays all current tasks with a number."""
    if not tasks:
        print("No tasks found. Add one first!")
        return

    print("\n--- Your Tasks ---")
    # 'enumerate' gives us a number (idx) for each item (task)
    # We add 1 to the index so the list starts at 1, not 0
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. [{task['status']}] {task['title']} ({task['priority']})")
    print("------------------\n")

def complete_task(tasks):
    """Marks a task as 'Complete'."""
    view_tasks(tasks) # Show the user the tasks first
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to complete: "))
        if 1 <= task_num <= len(tasks):
            # We subtract 1 to get the correct list index (which starts at 0)
            tasks[task_num - 1]["status"] = "Complete"
            print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    view_tasks(tasks) # Show the user the tasks first
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            # We subtract 1 to get the correct list index
            # .pop() removes the item from the list
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# --- STEP 4: THE MAIN MENU ---

def main():
    """The main function to run the task manager."""
    
    # Load tasks ONCE when the program starts
    tasks = load_tasks()

    while True:
        print("\n===== Task Manager Menu =====")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Save and Exit")
        print("=============================")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task(tasks)
            save_tasks(tasks) # Save after every change
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
            save_tasks(tasks) # Save after every change
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks) # Save after every change
        elif choice == "5":
            print("Goodbye!")
            break # This exits the 'while True' loop
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# This is a standard Python convention. 
# It means "run the main() function when this file is executed."
if __name__ == "__main__":
    main()