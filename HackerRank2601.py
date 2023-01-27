""" Question - 1

Given an array of integers, find the sum of its elements.
For example, if the array ar = [1,2,3], 1+2+3=6, so return 6.
"""

""" Solution {
arrlen = int(input())

arr = []

for i in range (0, arrlen):

    ele = int(input())

    arr.append(ele)

print(sum(arr))
    
 """   
  
  
##############################################################################################################################################  
    

""" Question - 2

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.
Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points."""


""" Solution

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice, bob = 0, 0
    for i in range(3):
        if a[i] < b[i]:
            bob += 1
        elif a[i] > b[i]:
            alice += 1
    return [alice, bob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""


################################################################################################################################################################
# Question 3


# Solution
""" 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    #Write your code here
    d_left = 0
    d_right = 0
    for i in range(len(arr)):
        d_left += arr[i][i]
    for j in range(len(arr)):
        d_right += arr[j][len(arr) -1-j]
        
    return abs(d_left - d_right)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
""" 

################################################################################################################################################################