#!/usr/local/bin/python3
import re

'''
    created by : Sangeeta Gupta
    objective : email validation for msc students
    assumptions : MSc SS and MSc CA started from the year 2000
'''
if __name__ == '__main__':
    email = input('Enter email id: ')
    pattern = re.compile('([1-9]{1}[0-9]*@20[0,1][0-9].(ca|ss).msc.sicsr.ac.in$)')
    answer = pattern.search(email)
    print(answer.group())
