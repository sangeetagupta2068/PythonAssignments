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
import logging
if __name__ == '__main__':

    file_read_object = ''
    file_write_object = ''
    logging.basicConfig(filename='python_code.log', filemode='w', format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    logging.info('root logged in')

    try:
        output_file_name = input('Enter file name:')
        file_write_object = open(output_file_name, 'w')
        file_read_object = open('/etc/passwd', 'r')
        file_content = file_read_object.readlines()

        for line in file_content:
            # line 1
            if line[0] != '#':
                file_write_object.write(line[:line.find(':')] + '\n')

        print('Successfully updated file!')

        file_write_object.close()

    except PermissionError as e:
        print("Sorry! Permission denied for file access.")
        logging.error("Exception occured",exc_info = True)

    except FileNotFoundError as e:
        print("Sorry couldn't find /etc/passwd file in your system")
        logging.error("Exception occured",exc_info = True)
        file_write_object.close()

    except IsADirectoryError as e:
        print("Expected file name as input but found directory!")
        logging.error("Exception occurred", exc_info = True)

    finally:
        logging.info('root logged out')