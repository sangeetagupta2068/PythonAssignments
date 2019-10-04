#!/usr/local/bin/python3

def largest_number(numbers : []) -> int:
    sum = 0
    numbers.sort(reverse = True)
    numbers = list(map(int,numbers))
    print(numbers)

    sum = 0
    for index in range(len(numbers)-1):
        if(len(str(numbers[index])) > len(str(numbers[index+1]))):
            numbers[index+1] = numbers[index+1] * 10
            print(numbers[index])
        else :
            if(len(str(numbers[index]))<len(str(numbers[index+1]))):
                numbers[index] = numbers[index]*10
                print(numbers[index])

        print(max(numbers[index]* 10 + numbers[index + 1], numbers[index + 1] * 10 + numbers[index]))
        # sum = sum * 10 + max(numbers[index]* 10 + numbers[index + 1], numbers[index + 1] * 10 + numbers[index])
        # print("Sun",sum)

def main():
    largest_number(['50','2','1','9','56','5'])
if __name__ == '__main__':
    main()