#!usr/local/bin/python3
import re
dict = {}
def odd_vowel_list(file_path:str):
    file_read_ptr = ''
    try:
        file_read_ptr= open(file_path,"r")
        file_lines = file_read_ptr.readlines()
        pattern = re.compile('[aeiou]')
        for line in file_lines:
            line = line.casefold()
            count = 0
            for letter in line :
                if pattern.search(letter):
                    count = count + 1
            if(count%2 != 0):
                if(count not in dict.keys()):
                    dict[count] = line
        file_read_ptr.close()

    except FileNotFoundError:
        print("Couldn't find file path")
    except IsADirectoryError:
        print("Given path is for a directory and not file")
        file_read_ptr.close()
    except PermissionError:
        print("You don't have read permission for file")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    odd_vowel_list('/Users/sangeetagupta/PycharmProjects/SICSRPythonAssignments/exam_answer_key/test_file')
    print(dict.values())