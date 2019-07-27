#!/usr/local/bin/python3
if __name__ == '__main__':
    input_list = [1,2,2,3,4,5,4]
    output_list = []

    for count in input_list:
        if count in output_list:
            continue
        output_list.append(count)

    print(output_list)

