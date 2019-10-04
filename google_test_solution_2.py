#!/usr/local/bin/python3

import sys
"""
    Author: Sangeeta Gupta
    Date : 7th September 2019
    Objective : to find the minimum load for the servers
"""
def minimum_load(A :[],count : int, calculated_load : int, total_load : int) -> int:

    if(count == 0):
        return abs((total_load - calculated_load) - calculated_load)
    else:
        return min(minimum_load(A,count -1,calculated_load + A[count -1],total_load),
                     minimum_load(A,count -1, calculated_load,total_load))

def solution(A : []) -> int:
  """Your solution goes here."""

  sum = 0
  total_size = len(A)
  for item in A:
      sum = sum + item

  return minimum_load(A,total_size,0,sum)

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()

