#!/usr/local/bin/python3

'''
    created by: Sangeeta Gupta
    created on: 17th August 2019
    objective: This program retrieves, prints all the system users username who donot have bash their default shell
               from the /etc/passwd file on the console and writes all retrieved usernames on a file namely
               passwd_username.txt
'''
import logging

if __name__ == '__main__':

    file_read_object = ''
    logging.basicConfig(filename='passwd_logger.txt', level=logging.DEBUG,
                        format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    logging.info('root logged in')

    try:

        file_read_object = open('/etc/passwd', 'r')
        username_list = [username[:username.find(':')] for username in file_read_object.readlines() if
                         '/bin/bash' not in username]

        print('List of users: ')
        for username in username_list:
            print(username)

        file_read_object.close()

    except PermissionError:
        print('Sorry! Permission denied for file access.')
        logging.error('Exception occured', exc_info=True)

    except FileNotFoundError:
        print('Sorry file/path to file doesn\'t exist')
        logging.error("Exception occured", exc_info=True)

    except IsADirectoryError:
        print('Expected file name as input but found directory!')
        logging.error('Exception occurred', exc_info=True)

    except Exception:
        print('Oops! Exception occurred')
        logging.info('Exception occurred', exc_info=True)

    finally:
        logging.info('root logged out')
