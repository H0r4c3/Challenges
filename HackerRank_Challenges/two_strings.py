'https://www.hackerrank.com/challenges/two-strings/problem?h_r=next-challenge&h_v=zen'

'''
Given two strings, determine if they share a common substring. A substring may be as small as one character.
'''

import math
import os
import random
import re
import sys

def twoStrings(s1, s2):
    common = [item for item in s1 if item in s2]
    
    return 'YES' if common else 'NO'
        
        
if __name__ == '__main__':
    assert twoStrings('hello', 'world') == 'YES'
    assert twoStrings('hi', 'world') == 'NO'
    print('Done!!!')