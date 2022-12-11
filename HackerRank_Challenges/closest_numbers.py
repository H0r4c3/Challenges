'https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true'

'''
Given a list of unsorted integers, , find the pair of elements that have the smallest absolute difference between them. 
If there are multiple pairs, find them all.
'''

import math
import os
import random
import re
import sys

#import itertools

def closestNumbers(arr):
    arr = sorted(arr)
    #pairs = list(itertools.pairwise(arr)) # if itertools not allowed
    pairs = list(zip(arr, arr[1:]))
    print(pairs)
    
    pairs_dict = {key:value for key, value in enumerate(pairs)}
    print(pairs_dict)
        
    differences = [abs(item[1] - item[0]) for item in pairs]
    print(differences)
    
    diff_min = min(differences)
    
    idx = [id for id, item in enumerate(differences) if item == diff_min]
    print(idx)
    
    result = list()
    for id in idx:
        for key, value in pairs_dict.items():
            if id == key:
                result.append(value)
    
    result_flat = [element for sublist in result for element in sublist]
          
    print(result_flat)
    return result_flat



if __name__ == '__main__':
    assert closestNumbers([1, 2, 3, 4, 6, 8, 9]) == [1, 2, 2, 3, 3, 4, 8, 9]
    assert closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]) == [-20, 30] # (30) - (-20) = 50, 
    # which is the smallest difference.
    assert closestNumbers([5, 4, 3, 2]) == [2, 3, 3, 4, 4, 5] # Here, the minimum difference is 1. Valid pairs are (2, 3), (3, 4), and (4, 5).
    
    print('Done!!!')