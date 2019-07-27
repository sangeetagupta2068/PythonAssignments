if __name__ == '__main__':
    file_ptr = open("data.txt", 'r')
    temp_file_content = file_ptr.readlines()

    write_ptr = open("data.txt", 'w')

    for line in temp_file_content:
       print(line[:10] + line[11:],end='',file=write_ptr)
        # use file_ptr.write() instead of print
    write_ptr.close()
    file_ptr.close()
#read file from user and delete that number wala character from file