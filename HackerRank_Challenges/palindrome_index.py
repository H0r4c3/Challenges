'https://www.hackerrank.com/challenges/palindrome-index/problem?isFullScreen=true'

'''
Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. 
There may be more than one solution, but any will do. 
If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Solution = Brute Force (NOK, time )

def check_palindrome(my_string):
    return my_string == my_string[ : : -1]


# My Solution:

def palindromeIndex(s):
    print(s)
    
    if check_palindrome(s):
        return -1
    
    s_backwards = s[::-1]
    
    both = list(zip(s, s_backwards))
    print(both)
    
    for i in range(len(s)):
        print(both[i][0])
        print(both[i][1])
        if both[i][0] != both[i][1]:
            s1 = s[ : i] + s[i+1 : ]
            j = len(s) - i
            s2 = s[ : j] + s[j+1 : ]
            print(s)
            if check_palindrome(s1):
                return i
            elif check_palindrome(s2):
                return j
    return -1



# Brute Force Solution (too long time for execution!):
def palindromeIndex_(s):
    if check_palindrome(s):
        return -1
    
    for i in range(len(s)):
        #new_s = s[:0] + s[1:] #eliminate the first char
        #print(new_s)
        #new_s = s[:1] + s[2:] #eliminate the second char
        #print(new_s)
        new_s = s[ : i] + s[i+1 : ]
        #print(new_s)
        if check_palindrome(new_s):
            return i
    
    return -1


if __name__ == '__main__':
    
    s = 'a2ba'
    result = palindromeIndex(s)
    
    print(result)
    
    assert palindromeIndex('a2ba') == 1
    assert palindromeIndex('aaab') == 3
    assert palindromeIndex('baa') == 0
    print('Done!!!')
    
    