#!usr/local/bin/python3

'''
    Objective:
    Date:
'''

def factorial(num:int)->int:
    if(num == 0):
        return 1
    if(num == 1):
        return num
    return num * factorial(num-1)


if __name__ == '__main__':
    try:
        num = int(input('Enter number: '))
        answer = factorial(abs(num))
        if(num< 0 and num%2 != 0):
            answer = answer * -1
        print(answer)

    except ValueError:
        print('Please enter integer number only')

