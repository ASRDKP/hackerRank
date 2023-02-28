#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
def breakingRecords(scores):
    # Write your code here
    maxscore = scores[0]
    minscore = scores[0]
    mincount = 0
    maxcount = 0
    for i in range(1,len(scores)):
        if scores[i] > maxscore:
            maxscore = scores[i]
            maxcount+=1
        if scores[i] < minscore:
            minscore = scores[i]
            mincount+=1
    return maxcount, mincount
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
