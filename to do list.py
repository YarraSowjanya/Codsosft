tasks = []

while True:
    choice = input("t1. Add Task\nt2. Remove Task\nt3. View Tasks\nt4. Exit\nEnter your choice: ")
    
    if choice == 't1':
        tasks.append(input("Enter the task: "))
    elif choice == 't2':
        task = input("Enter the task to remove: ")
        tasks.remove(task) if task in tasks else print("Task not found.")
    elif choice == 't3':
        print("\n".join(tasks) if tasks else "No tasks yet.")
    elif choice == 't4':
        break
    else:
        print("Invalid choice.")