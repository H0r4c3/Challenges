'https://www.hackerrank.com/challenges/anagram/problem?isFullScreen=true&h_r=next-challenge&h_v=zen'

'''
Given a string, split it into two contiguous substrings of equal length. 
Determine the minimum number of characters to change to make the two substrings into anagrams of one another.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    #split the string in 2 equal parts
    s1 = s[ : len(s) // 2]
    s2 = s[len(s) // 2 :]
    print(f's = {s}')
    print(f's1 = {s1}')
    print(f's2 = {s2}')
    
    if len(s1) != len(s2):
        return -1
    
    for char in s1:
        if char in s2:
            s2 = re.sub(char, '', s2, count=1)
            print(f's2 = {s2}')
            
    return len(s2)


if __name__ == '__main__':
    
    s = 'aaabbb'
    result = anagram(s)
    
    print(result)
    
    assert anagram('aaabbb') == 3
    assert anagram('xaxbbbxx') == 1
    assert anagram('xyyx') == 0
    assert anagram('abc') == -1
    print('Done!!!')