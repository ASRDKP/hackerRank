"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example arr = [1,3,5,7,9]

The minimum sum is 1+3+5+7 =16 and the maximum sum is 3+5+7+9 = 24 . The function prints

16 24

"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here

    arr.sort()

    min = arr[0]

    # print(min)

    max = arr[4]

    # print(max)

    min_result = 0

    for i in range(0, 4):
        min_result = min_result + arr[i]
        

    max_result = 0

    for i in range(1, 5):
        max_result = max_result + arr[i]
        
    print(min_result, max_result)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
