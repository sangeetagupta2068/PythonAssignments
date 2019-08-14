#!/usr/local/bin/python3

'''
    created by: Sangeeta Gupta (19030142029)
    created on: 14th August 2019
    objective: This program reads a text file and generates n-grams which would further serve as a means for building text prediction models.
'''

import re, logging

n_gram_list = []


def n_grams(sentences, n):
    count = 0
    sentences = re.sub(r'[^a-zA-Z0-9]', ' ', sentences).lower()
    sentence_list = [sentence for sentence in sentences.split(' ') if sentence]

    if n > len(sentence_list) or n < 1:
        raise Exception('n value cannot be greater than file word count, less than or equal to 0')

    while (len(sentence_list) - count >= n):
        n_gram_list.append(' '.join(sentence_list[count:count + n]))
        count = count + 1


if __name__ == "__main__":
    logging.basicConfig(filename='logger.txt', level=logging.DEBUG,
                        format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    logging.info('root logged in')
    file_read_object = ''

    try:
        input_file = input('Enter input file name: ')
        n = int(input('Enter n value: '))

        file_read_object = open(input_file, 'r')
        file_content = file_read_object.read()

        n_grams(file_content, n)
        print(n_gram_list)

    except TypeError:
        print("Position value should be an integer")
        logging.error("Exception occurred", exc_info=True)

    except PermissionError:
        print("You don't have permission to access file!")
        logging.error('Exception occurred', exc_info=True)

    except FileNotFoundError:
        print('File/path to file doesn\'t exist')
        logging.error('Exception occurred', exc_info=True)

    except IsADirectoryError:
        print('Expected file but found directory')
        logging.error('Exception occurred', exc_info=True)

    except Exception as e:
        print(str(e))
        logging.error(str(e))

    finally:
        logging.info('root logged out.')
