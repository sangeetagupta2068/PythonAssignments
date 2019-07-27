#!/usr/local/bin/python3

'''
    created by: Sangeeta Gupta (19030142029)
    created on: 27th July 2019
    objective: This program reads a an integer num from user and deletes the character which can be expressed as a multiple of num from a file called data.txt

'''

'''
    objective: this removes a character at position N where N is a multiple of num
               (int) -> (None)
'''
def remove_character(num):
    read_ptr = open('data.txt', 'r')
    file_content = read_ptr.readlines()
    file_content = ('').join(file_content)

    write_ptr = open('data.txt', 'w')

    for count in range(0, len(file_content), num):
        write_ptr.write(file_content[count:count + (num - 1)])

    write_ptr.close()
    read_ptr.close()

if __name__ == '__main__':
    num = int(input('Enter position: '))
    remove_character(num)
    print('File content successfully modified!')


