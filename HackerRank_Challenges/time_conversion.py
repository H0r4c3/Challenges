'https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=false'
'https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior'

'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
'''

import math
import os
import random
import re
import sys

from datetime import datetime

    
def timeConversion(s):
    s1 = datetime.strptime(s, "%I:%M:%S%p")
    
    return datetime.strftime(s1, "%H:%M:%S")


if __name__ == '__main__':
    
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    
    s = '06:00:00PM'

    result = timeConversion(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()


