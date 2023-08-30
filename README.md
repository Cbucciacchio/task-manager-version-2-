# Task Manager Capstone Project

## Overview
This application, named task-manager-version-2, is an updated and more functional task management system compared to its predecessor. It has been designed to store tasks in text files and provide different features to both regular users and admins. Using Python and its standard libraries, this program offers a command-line interface for task management functionalities such as adding tasks, viewing tasks, and more.

## Features
- Register New User (Admin Only): Admin can add a new username and password.
- Add Task: Allows users to add a new task with details like task title, description, and due date.
- View All Tasks: View all tasks in a formatted manner.
- View My Tasks: Users can view tasks specifically assigned to them.
- Edit Task: Users have the option to edit a task's status or re-assign it.
- Generate Reports: Generate reports to get statistics about tasks and users.
- Display Statistics (Admin Only): Shows the number of tasks and users in the system.

## Installation
- Clone the repository or download the zip file.
- Navigate to the directory containing the .py file in the terminal.
- Run the Python file using the command python <filename>.py.
  
## How to Use
1. First, log in using your username and password.
2. If you are an admin, you will see additional options in the menu for user registration and statistics.
3. Select the operation you want to perform (add task, view tasks, etc.) and follow the on-screen instructions.

## Technologies Used
- Python
- Python Standard Libraries (datetime, os)

## File Descriptions
- user.txt: Stores the username and password of registered users.
- tasks.txt: Contains information about tasks, such as the user it's assigned to, the title, description, due date, and status.
- task_overview.txt: Auto-generated report that gives an overview of task statistics.
- user_overview.txt: Auto-generated report that provides an overview of user statistics.

## Function Descriptions
- reg_user(): Register new users (Admin only).
- add_task(): Add a new task.
- view_all(): View all tasks.
- view_mine(): View tasks assigned to the logged-in user.
- edit_task(): Edit an existing task.
- generate_reports(): Generate reports about tasks and users.
- display_statistics(): Display statistical data (Admin only).
- admin_menu(): Menu interface for Admin.
