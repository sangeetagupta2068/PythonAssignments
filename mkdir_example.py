import os
if __name__ == '__main__':
    try:
        input_directory_path = input('Enter directory path: ')
        os.mkdir(input_directory_path,0o755)
    except OSError as e:
        print(e)

#FileExistsError
#PermissionError
#FileNotFoundError <-Directory path doesn't exist
