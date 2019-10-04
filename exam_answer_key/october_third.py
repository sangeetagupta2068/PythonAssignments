#!usr/local/bin/python3

import re
def generate_user_list(file_path : str)->list:
    file_ptr = ''
    list = []
    try:
        file_ptr = open(file_path,'r')
        user_details = file_ptr.readlines()
        pattern = re.compile('/bin/sh$')
        for line in user_details:
            if(pattern.search(line)):
                list.append(line[:-2])
        file_ptr.close()

    except FileNotFoundError as e:
        print(e)
    except IsADirectoryError as e:
        print(e)
        file_ptr.close()
    except PermissionError as e:
        print(e)
    except Exception as e:
        print(e)

    return list
if __name__ == '__main__':
    print(generate_user_list('/etc/passwd'))
