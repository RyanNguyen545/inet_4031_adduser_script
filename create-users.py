#!/usr/bin/python3

# INET4031
# Ryan Nguyen
# 10/23/2025
# 10/27/2025

#Imports necessary modules that interact with the operating system
import os
import re
import sys

def main():
    for line in sys.stdin:

        #This uses regex to check if the line starts with a '#' character. If it does, then the line will be skipped
        match = re.match("^#",line)

        #This splits the line into fields using ':' as the delimiter
        fields = line.strip().split(':')

        #If the current line starts with a '#' or if the number of fields is not equal to 5, skip to the next line
        if match or len(fields) != 5:
            continue

        #Assign the first field to username, the second to password, and the third and fourth field are formatted into a string.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Split the fifth field by commas to get a list of groups
        groups = fields[4].split(',')

        #Prints out a message indicating that an account is being made
        print("==> Creating account for %s..." % (username))
        #This line constructs the command to create a user with a disabled password and the provided infromation in the gecos string.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print cmd
        os.system(cmd)

        #Prints out a message indicating that the password is being set
        print("==> Setting the password for %s..." % (username))
        # This line constructs the command to set the password for the user using sudo privileges.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd
        os.system(cmd)

        for group in groups:
            #This if statement is checking if the group is not equal to '-'.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
