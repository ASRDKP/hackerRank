"""
"""


#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    
    keyboards.sort()
    drives.sort()

    extralist = []


    for keyboard in keyboards:
        for drive in drives:
            x = keyboard + drive
            if x <= b:
                extralist.append(x)

    if  (keyboards[0] + drives[0]) > b:
        x = -1
        return x
    else:
        x = max(extralist)
        return x    
        

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()











