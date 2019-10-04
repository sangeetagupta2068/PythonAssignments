#!/usr/local/bin/python3
'''
    Objective: to print unique sub directories in a directory
'''
import os
directory_list = []
filename_list = []
def generate_directory_list(directory_name : str):
    for path,directories,files in os.walk(directory_name):
        directory_list.extend(directories)
        filename_list.extend(files)

if __name__ == '__main__':
    try:
        generate_directory_list("/Users/sangeetagupta/Downloads/xyz")
        print(set(directory_list),end="\n\n\n")
        print(set(filename_list))

    except(OSError):
        print("Operating System error happened!")
    except(NotADirectoryError):
        print("Given file path isn't a directory!")
    except(FileNotFoundError):
        print("Couldn't find directory in specified path")