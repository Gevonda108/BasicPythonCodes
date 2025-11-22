import time
import random

print("=========================================")
print("Welcome to the To-Do List Application!")
print("Where you can manage your tasks efficiently.")
print("=========================================")
time.sleep(3)

todo_list = []

while True:
    print("\nSelect an option:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")

    elif choice == "2":
        task = input("Enter the task you want to add: ")
        todo_list.append(task)
        print(f'Task "{task}" added to your to-do list.')

    elif choice == "3":
        if not todo_list:
            print("Your to-do list is empty. No tasks to remove.")
        else:
            print("Your To-Do List:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")
            task_num = int(input("Enter the task number you want to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f'Task "{removed_task}" removed from your to-do list.')
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting the To-Do List Application. Goodbye!")
        break

    else:
        print("Invalid input. Please choose a valid option.")
    time.sleep(2)