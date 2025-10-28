# INET 4031 Add User Script

# Program Description
This repository contains a Python script to automatically add users on an Ubuntu system. 

# Program User Operations
This program works by taking a user-prepared input file that contains all the necessary details, and the script will iterate through the file and construct the necessary commands needed to add each user to the server.

# Input file format
The input file is a plain text file where each line represents a user and contains five fields. The first field is the username, the second field is password, the third field is last name, the fourth field is first name, and the last field is the groups.

# Command Execution
Make sure the permission is set so the python file can be executable. Then to execute the command user ./create-users.py < create-users.input

# Dry Run
If you were to do a Dry Run of the code it will process the input file and print to the screen status messages.
