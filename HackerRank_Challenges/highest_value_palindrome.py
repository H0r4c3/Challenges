'https://www.hackerrank.com/challenges/richie-rich/problem?h_r=internal-search&h_r=next-challenge&h_v=zen'

'''
Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string 
of digits possible or the string '-1' if it is not possible to create a palindrome under the constraints.
'''

import math
import os
import random
import re
import sys


def highestValuePalindrome(s, n, k):
    
    
    return -1

if __name__ == '__main__':
    assert highestValuePalindrome('3943', 4, 1) == '3943' # 3993 > 3943
    assert highestValuePalindrome('092282', 6, 3) == '992299'
    print('Done!!!')