
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if (year % 4 == 0) and (year < 1918):
        x = "12.09." + str(year)
        return x
    elif (year % 400 ==0) and (year % 100 != 0):
        x = "12.09." + str(year)
        return x
    elif (year == 1918):
        x = "26.09." + str(year)
        return x 
    else:
        x = "13.09." + str(year)
        return x

if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)

