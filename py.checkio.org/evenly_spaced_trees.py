'https://py.checkio.org/en/mission/evenly-spaced-trees/'

'''
You are given a list of integers as an input value. This is the position of an existing tree. 
You must return the minimum number of additional trees needed so that they could be evenly spaced.

Positions of the existing trees are already sorted.
All positions of trees are integers.
'''

import math
from typing import List

# Solution 1
def evenly_spaced_trees_(trees: List[int]) -> int:
    xdiff = [trees[i] - trees[i-1] for i in range(1, len(trees))]
    #print(xdiff)
    
    gcdiv = math.gcd(*xdiff)
    print(gcdiv)
    
    for item in xdiff:
        result += item // gcdiv - 1
    
    return result


# Solution 2
import numpy as np
import functools
def evenly_spaced_trees(trees: List[int]) -> int:
    xdiff = np.diff(trees)
    print(xdiff)
    
    gcdiv = math.gcd(*xdiff)
    
    result = sum([item // gcdiv - 1 for item in xdiff])
    
    print(result)
    return result
    
    
# Solution 3  
from itertools import pairwise   
def evenly_spaced_trees_(trees: List[int]) -> int:
    result = 0
    pairs = pairwise(trees)
    
    xdiff = [y-x for (x,y) in pairs]
    print(xdiff)
    
    gcdiv = math.gcd(*xdiff)
    print(gcdiv)
    
    for item in xdiff:
        result += item // gcdiv - 1
    
    return result


# Best Solution:
# https://py.checkio.org/mission/evenly-spaced-trees/publications/veky/python-3/obvious/?ordering=most_voted&filtering=all
import operator, functools, math

def evenly_spaced_trees(trees):
    spaces = [*map(operator.sub, trees[1:], trees)]
    delta = functools.reduce(math.gcd, spaces)
    return sum(d // delta - 1 for d in spaces)


if __name__ == '__main__':
    print("Example:")
    #print(evenly_spaced_trees([0, 2, 6]))
    assert evenly_spaced_trees([0, 2, 6]) == 1, 'add 1'
    assert evenly_spaced_trees([1, 3, 6]) == 3, 'add 3'
    assert evenly_spaced_trees([0, 2, 4]) == 0, 'no add'
    print("Coding complete? Click 'Check' to earn cool rewards!")