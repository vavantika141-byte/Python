tasks = []
while True:
    print("TASK MANAGER")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete task")
    print("5. Exit from the Task")

    choice = input("Enter your Choice: ").strip() # to remove whitespaces

    if choice=="1":
        task=input("Enter the task: ")
        tasks.append({"task": task, "done": False})
        print("Task added")

    elif choice=="2":
        if len(tasks)==0:
            print("NO TASK FOUND")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                if task["done"]:       
                    status = "+"
                else:
                    status = "-"
                print(i,".",task["task"],f"[{status}]")

    elif choice=="3":
        if len(tasks)==0:
            print("No task found.")
        else:
            print("\nYour tasks:")
            for i,task in enumerate(tasks, 1):
                if task["done"]:       
                    status="+"
                else:
                    status="-"
                print(i, ".", task["task"], f"[{status}]")
            n = int(input("Enter number of task to complete: "))
            if n >= 1 and n <= len(tasks):
                tasks[n - 1]["done"] = True
                print("Task completed.")
            else:
                print("Invalid.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, 1):
                if task["done"]:
                    status = "+"
                else:
                    status = "-"
                print(f"{i}. {task['task']} [{status}]")
            n = int(input("Enter number of task to delete: ")).strip()
            if n >= 1 and n <= len(tasks):  
                tasks.pop(n - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting from the Task Manager.")
        break

    else:
        print("INVALID CHOICE.")