'https://py.checkio.org/en/mission/expand-intervals/'

'''
An interval of consecutive positive integers can be succinctly described as a tuple that contains first and last values. 
For example, the interval that contains the numbers 5, 6, 7, 8, 9 can be described as (5,9). Multiple intervals can be united together into iterable. Given an an iterable with intervals (guaranteed not to overlap with each other and to be listed in a sorted ascending order), create and return the list that contains all the integers contained by these intervals.

Input: The iterable of tuples of two integers.

Output: The iterable of integers.
'''

from typing import Iterable

def expand_intervals_(items: Iterable) -> Iterable:
    result = list()
    for item in items:
        result.extend(range(item[0], item[-1] + 1))
    
    print(result)
    
    return(result)


# Best Solution:
# https://py.checkio.org/mission/expand-intervals/publications/oduvan/python-3/simple-yield/

def expand_intervals(items: Iterable) -> Iterable:
    for item in items:
        for i in range(item[0], item[1] + 1):
            yield i


if __name__ == '__main__':
    print("Example:")
    print(list(expand_intervals([(1, 3), (5, 7)])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(expand_intervals([(1, 3), (5, 7)])) == [1, 2, 3, 5, 6, 7]
    assert list(expand_intervals([(1, 3)])) == [1, 2, 3]
    assert list(expand_intervals([])) == []
    assert list(expand_intervals([(1, 2), (4, 4)])) == [1, 2, 4]