# Question 4

"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000 
"""

# Solution

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    size = len(arr)
    
    p = 0
    n = 0
    z = 0
    
    for i in range(0, size):
        if arr[i] > 0:
            p = p + 1
        elif arr[i] < 0:
            n = n + 1
        else:
            z = z + 1
    
    po = p/size
    no = n/size
    zo = z/size

    print(f"{po:.6f}")
    print(f"{no:.6f}")
    print(f"{zo:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)



