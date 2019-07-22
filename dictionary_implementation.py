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
def dictionary_convert(prn_room_dictionary):
    room_prn_dictionary = {}
    unique_room_number_list = set(prn_room_dictionary.values())

    for room_number in unique_room_number_list:
        room_prn_dictionary[room_number] = []

    for prn in prn_room_dictionary.keys():
        room_prn_dictionary.get(prn_room_dictionary.get(prn)).append(prn)

    return room_prn_dictionary


if __name__ == "__main__":
    initial_time_taken = time.time()

    prn_room_dictionary = {
        '16030121116': 101,
        '16030121112': 101,
        '19030142001': 102,
        '19030142002': 102,
        '19030141015': 103,
        '19030121113': 103,
        '19030122007': 103,
    }
    print(dictionary_convert(prn_room_dictionary))

    print(time.time() - initial_time_taken)
