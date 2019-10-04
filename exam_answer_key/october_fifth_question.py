#!usr/local/bin/python3

import re

def sort_file(file_read_path: str, file_write_path: str) -> None:
    try:
        file_read_ptr = open(file_read_path, 'r')
        file_write_ptr = open(file_write_path, 'w')

        pin_pattern = re.compile(r'[1-9]\d{5}')
        name_pattern = re.compile(r'[A-Z][a-z]+ [a-z]+')
        phone_pattern = re.compile(r'[6789]\d{9}')

        for line in file_read_ptr.readlines():
            name = re.findall(name_pattern, line)
            phone = re.findall(phone_pattern, line)
            pin = re.findall(pin_pattern, line)

            if(len(pin)!= 0 and len(phone)!=0):
                for item in pin:
                    if item in phone[0]:
                        pin.remove(item)
                if(len(name)!=0 and len(pin)!=0):
                    file_write_ptr.write(name[0] + ',' + phone[0] + ',' + pin[0] + "\n")

        file_write_ptr.close()
        file_read_ptr.close()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    sort_file('/Users/sangeetagupta/PycharmProjects/SICSRPythonAssignments/exam_answer_key/regex_test_file',
              '/Users/sangeetagupta/PycharmProjects/SICSRPythonAssignments/exam_answer_key/regex_output_test_file.txt')
