#!/usr/local/bin/python3

'''
    created by: Sangeeta Gupta (19030142029)
    created on: 14th August 2019
    objective: This program takes a list function name from user and thus implements the same.
'''

import logging

if __name__ == '__main__':
    logging.basicConfig(filename='logger.txt', level=logging.DEBUG,
                        format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    logging.info('root logged in')

    values = []

    size = int(input('Enter list size:'))
    for count in range(size):
        value = input('Enter list item: ')
        values.append(value)

    print(values)

    function_name = input('Enter list function name: ')
    try:
        result = ''
        if hasattr(values,function_name):
            if (function_name in ('remove', 'append', 'count', 'index', 'pop')):
                item = input('Enter item value: ')
                result = getattr(values, function_name)(item)
            else:
                if (function_name == 'extend'):
                    values_to_be_extended = []
                    list_size = int(input('Input list size for extension: '))
                    for i in range(list_size):
                        value = input('Enter list item: ')
                        values_to_be_extended.append(value)
                    result = getattr(values, function_name)(values_to_be_extended)
                if (function_name == 'insert'):
                    item = input('Enter item value: ')
                    pos = int(input('Enter item position: '))
                    result = getattr(values, function_name)(pos, item)
                else:
                    result = getattr(values, function_name)()

    except AttributeError:
        print('Attribute error occured')
        logging.error("Exception occurred", exc_info=True)

    except ValueError:
        print('Value error occured')
        logging.error("Exception occurred", exc_info=True)

    except TypeError:
        print('Type error occured')
        logging.error("Exception occurred", exc_info=True)

    except IndexError:
        print('Index error occured')
        logging.error("Exception occurred", exc_info=True)

    except Exception as e:
        print(str(e))
        logging.error("Exception occurred", exc_info=True)

    finally:
        if (result != None):
            print(result)
        print(values)
        logging.info('root logged out.')
