'https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_r=internal-search'

'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. 
Given a string , determine if it is valid. If so, return YES, otherwise return NO.
'''

import math
import os
import random
import re
import sys

from collections import Counter


def isValid(s):
    char_counts = Counter(s)
    appearances = dict(char_counts.most_common())
    print(appearances)
    
    app_list = [value for key, value in appearances.items()]
    print(app_list)
    
    app_counts = Counter(app_list)
    app_final = list(app_counts.values())
    print(app_final)
    
    if len(app_final) == 1:
        return 'YES'
    
    if len(app_final) > 2:
        return 'NO'
    
    if len(app_final) == 2 and 1 in app_final:
        if (abs(app_list[0] - app_list[-1]) == 1):
            return 'YES'
        else:
            return 'NO'
    elif len(app_final) == 2 and 1 not in app_final:
        return 'NO'
    
    

import math
import os
import random
import re
import sys

from collections import Counter


def isValid_(s):
    from collections import Counter
    count = Counter(s)
    # if valid from start
    if all([count[c]==count[s[0]] for c in s]):
        return 'YES'
    else:
        # get max and min char
        max_char = [c for c in s if count[c]==max(count.values())][0]
        min_char = [c for c in s if count[c]==min(count.values())][0]
        # remove 1 max char and test again
        count_max = count.copy()
        count_max[max_char] -= 1
        if all([count_max[c]==count[s[0]] for c in s]):
            return 'YES'
        # remove 1 min char and test again
        count_min = count.copy()
        count_min[min_char] -= 1
        if all([count_min[c]==count[s[0]] for c in s if count_min[c] != 0]):
            return 'YES'
        # if nothing worked, return 'NO'
        return 'NO'
    
    

if __name__ == '__main__':
    assert isValid('aabbccddeefghi') == 'NO'
    assert isValid('abcdefghhgfedecba') == 'YES'
    assert isValid('aabbccdddd') == 'NO'
    print('Done!!!')