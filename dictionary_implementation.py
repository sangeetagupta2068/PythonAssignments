#!/usr/local/bin/python3

'''
    created by: Sangeeta Gupta(19030142029)
    created on: 20th July 2019
    last modified on: 22nd July 2019
    objective: This program takes an input dictionary with key:value pair as prn:room_number,converts and prints a dictionary with key:value pair as room_no:prn
'''

import time

'''
    objective: this takes dictionary with prn:room_number  as a parameter and returns a dictionary with room_number:prn
               (dictionary) -> (dictionary)
'''

import logging


def dictionary_convert(prn_room_dictionary):
    room_prn_dictionary = {}
    unique_room_number_list = set(prn_room_dictionary.values())

    for room_number in unique_room_number_list:
        room_prn_dictionary[room_number] = []

    for prn in prn_room_dictionary.keys():
        room_prn_dictionary.get(prn_room_dictionary.get(prn)).append(prn)

    return room_prn_dictionary


if __name__ == "__main__":
    logging.basicConfig(filename='logger.txt', level=logging.DEBUG,
                        format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    logging.info('root logged in')

    try:
        size = int(input('Enter total item count for your dictionary:'))
        prn_room_dictionary = {}

        for count in range(size):
            key_value = input('Enter Student PRN: ')
            room_value = input('Enter Student Room number: ')
            prn_room_dictionary[key_value] = room_value

        print(dictionary_convert(prn_room_dictionary))

    except KeyError:
        print('Key couldn\'t be found!')
        logging.info('Exception occurred', exc_info=True)

    except TypeError:
        print('Expected integer as input for size')
        logging.info('Exception occurred', exc_info=True)

    except Exception:
        print('Oops! Exception occurred')
        logging.info('Exception occurred', exc_info=True)

    finally:
        logging.info('root logged out.')
