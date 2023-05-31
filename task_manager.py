#=====importing libraries===========

from datetime import date, datetime
import os
#====function definitions====

def reg_user():
    new_username = input("Please enter a new username: ")
    with open("user.txt", "r") as file:
        users = file.read()
        if new_username in users:
            print("Username already exists. Try a different username.")
            return
    new_password = input("Please enter a new password: ")
    new_password_check = input("Please confirm the password: ")
    if new_password == new_password_check: #if both passwords match then add to the user.txt file 
        with open("user.txt", "a") as file:
            new_user = f"{new_username}, {new_password}\n"
            file.write(new_user)
            print("User added successfully.")
    else:
        print("Password confirmation failed. Please try again.")

def add_task():
    new_task_user = input("Please enter the username of the person the task is assigned to: ")
    new_task_title = input("Please enter a title for this task: ")
    new_task_desc = input("Please describe this task: \n")
    
    # Get date in "DD MMM YYYY" format and convert to "YYYY-MM-DD" format
    new_task_duedate = input("Please enter the due date for this task (YYYY MM DD): ")
    new_task_duedate = datetime.strptime(new_task_duedate, '%d %b %Y').date().isoformat()
    
    new_task_curdate = date.today().isoformat()  # Get current date in "YYYY-MM-DD" format
    new_task_done = "No"
    
    with open("tasks.txt", "a") as file:
        new_task_all = f"{new_task_user}, {new_task_title}, {new_task_desc}, {new_task_duedate}, {new_task_curdate}, {new_task_done}\n"
        file.write(new_task_all)
        print("Task added successfully.")

def view_all():
    with open("tasks.txt", "r") as f:# open the tasks.txt file to read the tasks
        for line in f:# iterate over each line in the file and print the tasks in the desired format
            task_user, task_title, task_desc, task_duedate, task_curdate, task_done = line.strip().split(", ")
            print(f"Task assigned to: \t {task_user}")
            print(f"Task title: \t\t {task_title}")
            print(f"Task description: \t {task_desc}")
            print(f"Task due date: \t\t {task_duedate}")
            print(f"Task current date: \t {task_curdate}")
            print(f"Task complete? \t\t {task_done}")
            print("-" * 50)

def view_mine(username):
    tasks = []
    with open("tasks.txt", "r") as f: # open the tasks.txt file to read the tasks
        for line in f: # iterate over each line in the file and print the tasks in the desired format
            task_user, task_title, task_desc, task_duedate, task_curdate, task_done = line.strip().split(", ")
            if task_user == username:
                tasks.append(line.strip())
                print(f"- {len(tasks)} - \nTask title: \t\t {task_title}")
                print(f"Task description: \t {task_desc}")
                print(f"Task due date: \t\t {task_duedate}")
                print(f"Task current date: \t {task_curdate}")
                print(f"Task complete? \t\t {task_done}")
                print("-" * 50)
    task_num = input("Enter task number to edit or -1 to return to the main menu: ")
    if task_num != "-1":
        edit_task(tasks[int(task_num) - 1])

def edit_task(task_line):
    task_user, task_title, task_desc, task_duedate, task_curdate, task_done = task_line.split(", ")
    if task_done == "No":
        edit_choice = input("Enter 1 to mark as complete or 2 to edit the task: ")
        if edit_choice == "1":
            task_done = "Yes"
        elif edit_choice == "2":
            new_username = input("Enter a new username or -1 to skip: ")
            if new_username != "-1":
                task_user = new_username
            new_duedate = input("Enter a new due date or -1 to skip: ")
            if new_duedate != "-1":
                task_duedate = new_duedate
        else:
            print("Invalid choice.")
    else:
        print("Task is already completed and can't be edited.")
    
    # Write back the changes to the file
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    with open("tasks.txt", "w") as f:
        for line in lines:
            if line.strip() == task_line:
                f.write(f"{task_user}, {task_title}, {task_desc}, {task_duedate}, {task_curdate}, {task_done}\n")
            else:
                f.write(line)


def generate_reports():
    # read all tasks
    with open('tasks.txt', 'r') as f:
        lines = f.readlines()
    tasks = [line.strip().split(", ") for line in lines]
    
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task[5] == 'Yes'])
    uncompleted_tasks = len([task for task in tasks if task[5] == 'No'])
    overdue_tasks = len([task for task in tasks if task[5] == 'No' and date.today() > date.fromisoformat(task[3])])
    incomplete_percentage = round((uncompleted_tasks / total_tasks) * 100, 2)
    overdue_percentage = round((overdue_tasks / total_tasks) * 100, 2)

    with open('task_overview.txt', 'w') as f:
        f.write(f'Total number of tasks: {total_tasks}\n')
        f.write(f'Total number of completed tasks: {completed_tasks}\n')
        f.write(f'Total number of uncompleted tasks: {uncompleted_tasks}\n')
        f.write(f'Total number of tasks that are overdue and uncompleted: {overdue_tasks}\n')
        f.write(f'Percentage of tasks that are incomplete: {incomplete_percentage}%\n')
        f.write(f'Percentage of tasks that are overdue: {overdue_percentage}%\n')

    # read all users
    with open('user.txt', 'r') as f:
        lines = f.readlines()
    users = [line.strip().split(", ")[0] for line in lines]

    total_users = len(users)

    with open('user_overview.txt', 'w') as f:
        f.write(f'Total number of users: {total_users}\n')
        f.write(f'Total number of tasks: {total_tasks}\n')

        for user in users:
            user_tasks = [task for task in tasks if task[0] == user]
            user_total_tasks = len(user_tasks)
            user_tasks_completed = len([task for task in user_tasks if task[5] == 'Yes'])
            user_tasks_uncompleted = len([task for task in user_tasks if task[5] == 'No'])
            user_tasks_overdue = len([task for task in user_tasks if task[5] == 'No' and date.today() > date.fromisoformat(task[3])])
            user_task_percentage = round((user_total_tasks / total_tasks) * 100, 2)
            user_task_completed_percentage = round((user_tasks_completed / user_total_tasks) * 100, 2) if user_total_tasks != 0 else 0
            user_task_uncompleted_percentage = round((user_tasks_uncompleted / user_total_tasks) * 100, 2) if user_total_tasks != 0 else 0
            user_task_overdue_percentage = round((user_tasks_overdue / user_total_tasks) * 100, 2) if user_total_tasks != 0 else 0

            f.write(f'\nUser: {user}\n')
            f.write(f'Total number of tasks assigned: {user_total_tasks}\n')
            f.write(f'Percentage of the total number of tasks assigned: {user_task_percentage}%\n')
            f.write(f'Percentage of tasks assigned that are completed: {user_task_completed_percentage}%\n')
            f.write(f'Percentage of tasks assigned that are uncompleted: {user_task_uncompleted_percentage}%\n')
            f.write(f'Percentage of tasks assigned that are overdue and uncompleted: {user_task_overdue_percentage}%\n')


def display_statistics():
    if not os.path.exists('task_overview.txt') or not os.path.exists('user_overview.txt'):
        generate_reports()

    print("\nTask Overview:")
    with open('task_overview.txt', 'r') as f:
        print(f.read())

    print("\nUser Overview:")
    with open('user_overview.txt', 'r') as f:
        print(f.read())

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Register a user")
        print("2. Add a task")
        print("3. View all tasks")
        print("4. View my tasks")
        print("5. Display Statistics")
        print("6. Generate Reports")
        print("7. Exit")

        option = input("Select an option: ")
        if option == '1':
            reg_user()
        elif option == '2':
            add_task()
        elif option == '3':
            view_all()
        elif option == '4':
            view_mine(username)
        elif option == '5':
            display_statistics()
        elif option == '6':
            generate_reports()
        elif option == '7':
            print("Goodbye!")
            exit()
        else:
            print("Invalid option, please try again.")


#====Login Section====

with open("user.txt", "r") as f: # open user.txt file to read usernames and passwords
    users = {} # read all lines from file and create a dictionary of usernames and passwords
    for line in f:
        username, password = line.strip().split(", ")
        users[username] = password

while True: # use a while loop to keep asking for login details until they are valid
    username = input("Enter your username: ") # get username and password from  user
    password = input("Enter your password: ")

    if username in users and users[username] == password: # check if the username exists and the password is correct
        print("Welcome!")
        break  # exit the loop if the login details are valid
    elif username not in users:
        print("Invalid username. Please try again.")
    else:
        print("Invalid password. Please try again.")


while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username != 'admin':
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
e - Exit
: ''').lower()

        if menu == 'a': #adding a new task
            add_task()

        elif menu == 'va': #viewing all the tasks
            view_all()

        elif menu == 'vm': #veiwing the tasks depending on the user that is logged in 
            view_mine(username)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        elif menu == 'gr':
            generate_reports()
            print("Reports generated successfully.")

        else:
            print("You have made a wrong choice, Please Try again")
    
    if username == 'admin':
        admin_menu()