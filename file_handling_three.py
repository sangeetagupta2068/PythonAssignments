#!/usr/local/bin/python3

'''
    created by: Sangeeta Gupta
    created on: 17th August 2019
    objective: This program retrieves user information from a csv file and performs various operations on the same
'''
import logging


class User(object):

    def __init__(self, firstname, surname, contact_number):
        self.firstname = firstname
        self.surname = surname
        self.contact_number = contact_number

    def get_user_details(self):
        return self.firstname + ' ' + self.surname + ' ' + self.contact_number


if __name__ == '__main__':

    file_read_object = ''
    logging.basicConfig(filename='logger.txt', level=logging.DEBUG,
                        format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    logging.info('root logged in')

    try:
        csv_file_name = input('Enter file path: ')
        file_read_object = open(csv_file_name, 'r')
        user_list = []
        user_information = file_read_object.readlines()

        del user_information[0]
        user_information[len(user_information) - 1] = user_information[len(user_information) - 1] + '\n'

        for buffer_user in user_information:
            buffer_user = buffer_user.split(',')
            user = User(buffer_user[0], buffer_user[1], buffer_user[2])
            user_list.append(user)

        print('\nUsers whose first name letter and last name letter difference is atleast 5: ')
        for buffer_user in user_list:
            if abs(ord(buffer_user.firstname[0]) - ord(buffer_user.surname[0])) >= 5:
                print(buffer_user.get_user_details(), end='')

        print('\nUsers whose phone number\'s first and last digit is odd: ')
        for buffer_user in user_list:
            if (int(buffer_user.contact_number[0]) % 2 == 1 and int(
                    buffer_user.contact_number[len(buffer_user.contact_number) - 2]) % 2 == 1):
                print(buffer_user.get_user_details(), end='')

        print('\nUser surnames where user phone number don\'t start with 9:')
        for buffer_user in user_list:
            if (buffer_user.contact_number[0] != '9'):
                print(buffer_user.surname)

        print('\nUsers whose surname length is atleast 4 and third character lies between a and m')
        for buffer_user in user_list:
            if (buffer_user.surname[2] >= 'a' and buffer_user.surname[2] <= 'm' and len(buffer_user.surname) > 3):
                print(buffer_user.get_user_details(), end='')

        buffer_user_list = []
        print('\nUser list with unique first name: ')
        for buffer_user in user_list:
            if (buffer_user.firstname not in buffer_user_list):
                print(buffer_user.get_user_details(),end='')
                buffer_user_list.append(buffer_user.firstname)

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
