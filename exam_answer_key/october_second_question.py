#!usr/local/bin/python3

flatten_list = []
def generate_flatten_list(integer_list:list):
    for num in integer_list:
        if(type(num) == int):
            flatten_list.append(num)
        if(type(num) == list):
            return generate_flatten_list(num)


if __name__ == '__main__':
    generate_flatten_list([1,2,[3,5,[6,7]]])
    print(flatten_list)