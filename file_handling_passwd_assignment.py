#!/usr/local/bin/python3

'''
    created by: Sangeeta Gupta
    created on: 28th July 2019
    objective: This program retrieves, prints all the system users username from the /etc/passwd file on the console
               and writes all retrieved usernames on a file namely passwd_username.txt
    Additional Info: The /etc/passwd in Mac OS contains comments describing that the file is only consulted when
                     system is running on single user mode. Else, user information is provided by Open directory.
                     Hence, on line 1 a check is provided in order to distinguish the comment from user information.

'''

if __name__ == '__main__':
    file_read_object = open('/etc/passwd', 'r')
    file_write_object = open('passwd_username.txt', 'w')
    file_content = file_read_object.readlines()

    for line in file_content:
        # line 1
        if line[0] != '#':
            file_write_object.write(line[:line.find(':')] + '\n')

    print('Successfully updated passwd_username.txt file!')

    file_read_object.close()
    file_write_object.close()
