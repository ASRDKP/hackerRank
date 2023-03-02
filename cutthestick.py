#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    temp = []
    while True:
        temp.append(len(arr))
        shortest = min(arr)
        i = 0
        while i < len(arr):
            arr[i] = arr[i] - shortest
            if arr[i] == 0:
                arr.remove(arr[i])
                i = i - 1
            i = i + 1
        if len(arr) == 0:
            break
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
