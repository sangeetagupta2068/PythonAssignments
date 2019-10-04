#!/usr/local/bin/python3
import sys


def solution(N: [], K: int) -> []:
    index_sum_pair = {}
    for index in range(len(N) + 1 - K):
        sum = 0
        for item in N[index:index + K]:
            sum = sum + item
        index_sum_pair[index] = sum

    start = max(index_sum_pair, key=index_sum_pair.get)
    return N[start:start + K]


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    input = sys.stdin.readline().split()
    N = [int(x) for x in input[0].split(",")]
    K = int(input[1])
    solution(N, K)
    sys.stdout.write(",".join([str(i) for i in solution(N, K)]))


if __name__ == "__main__":
    main()

