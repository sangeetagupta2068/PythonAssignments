#!/usr/local/bin/python3

'''
    created by: Sangeeta Gupta (19030142029)
    created on: 27th July 2019
    objective: This program reads a an integer num from user and deletes the character which can be expressed as a multiple of num from a file called input_data.txt
               and writes the changed data to a file called output_data.txt

'''

import logging

if __name__ == '__main__':
    logging.basicConfig(filename='logger.txt', level=logging.DEBUG,
                        format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    logging.info('root logged in')
    file_read_object = ''
    file_write_object = ''

    try:
        input_file = input('Enter input file name: ')
        output_file = input('Enter output file name: ')
        num = int(input('Enter position: '))

        file_read_object = open(input_file, 'r')
        file_write_object = open(output_file, 'w')

        file_content = file_read_object.readlines()
        file_content = ('').join(file_content)

        for count in range(0, len(file_content), num):
            file_write_object.write(file_content[count:count + (num - 1)])

        file_write_object.close()
        file_read_object.close()

        print(output_file,'successfully updated')
        logging.info(output_file,'successfully updated')

    except TypeError:
        print("Position value should be an integer")
        logging.error("Exception occurred",exc_info=True)

    except PermissionError:
        print("You don't have permission to access file!")
        logging.error('Exception occurred',exc_info = True)
        if(type(file_read_object) != type('')):
            file_read_object.close()

    except FileNotFoundError:
        print('File/path to file doesn\'t exist')
        logging.error('Exception occurred',exc_info=True)

    except IsADirectoryError:
        print('Expected file but found directory')
        logging.error('Exception occurred', exc_info=True)

    except Exception:
        print('Oops! Exception occurred')
        logging.info('Exception occurred',exc_info = True)

    finally:
        logging.info('root logged out.')
