"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s= '12:01:00PM'

Return '12:01:00'.

s= '12:01:00AM'
Return '00:01:00'.

"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    hour = int(s[:2:])
    current_time = s[:-2:]
    remainig_time = s[2:]
    remainig_time = remainig_time[:-2:]
    # print(remainig_time)

    if s[-2:] == 'PM':
        if hour == 12:
            return (current_time)
        else:   
            hour = hour + 12      
            current_time = str(hour) + remainig_time
            if hour < 12:
                return ('0' + current_time)
            else:
                return current_time
            
        
    else:
        if hour == 12:
            return ("00" + remainig_time)
        else:
            return current_time
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
