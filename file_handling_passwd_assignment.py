#!/usr/local/bin/python3

'''
    created by: Sangeeta Gupta
    created on: 28th July 2019
    objective: This program retrieves and prints all the system users username from the /etc/passwd file
    Additional Info: The /etc/passwd in Mac OS contains comments describing that the file is only consulted when
                     system is running on single user mode. Else, user information is provided by Open directory.
                     Hence, on line 1 a check is provided in order to distinguish the comment from user information.

'''

if __name__ == '__main__':
    file_read_object = open('/etc/passwd', 'r')
    file_content = file_read_object.readlines()

    print('List of usernams in /etc/passwd file are:')
    for line in file_content:
        #line 1
        if line[0] != '#':
            print(line[:line.find(':')])

    file_read_object.close()
