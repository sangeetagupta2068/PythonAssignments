#!/usr/local/bin/python3

if __name__ == '__main__':
    try:
        input_file = open("test.txt","r")
        #path(w/r) or file doesn't exist(r) : [Errno 2] No such file or directory: '/abc/test.txt'
        #No permission to write at root : [Errno 13] Permission denied: '/test.txt'

    except Exception as e :
        print(e)

