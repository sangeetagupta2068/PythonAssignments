#!/usr/local/bin/python3
import sys


def solution(A: str, B: str) -> []:
    """Your solution goes here."""
    frequency_A = []
    frequency_B = []
    frequency = []

    A = A.split(',')
    B = B.split(',')

    for item in A:
        ''.join(sorted(item))
        frequency_A.append(item.count(item[0]))

    for item in B:
        ''.join(sorted(item))
        frequency_B.append(item.count(item[0]))

    for frequency_value in frequency_B:
        frequency.append(len([value for value in frequency_A if value < frequency_value]))

    return frequency


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    input = sys.stdin.readline().split()
    A = input[0]
    B = input[1]
    solution(A, B)
    sys.stdout.write(",".join([str(i) for i in solution(A, B)]))


if __name__ == "__main__":
    main()
