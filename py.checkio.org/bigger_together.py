'https://py.checkio.org/en/mission/bigger-together/'

'''
Your mission here is to find a difference between the maximally positive and maximally negative numbers. 
Those numbers can be found by concatenating the given array of numbers.

Let’s check an example. If you have numbers 1,2,3, then 321 is the maximum number, and 123 - is the minimum. 
The difference between those numbers is 198. But if you have numbers 4, 3 and 12 then 4312 is the maximum number, and 1234 - is the minimum.
'''

from typing import List
from functools import cmp_to_key

def bigger_together_(ints: List[int]) -> int:
    """
        Returns difference between the largest and smallest values
        that can be obtained by concatenating the integers together.
    """
    def suma(x, y):
        return int(x + y) - int(y + x)
     
    ints_str = map(str, ints)
    print(ints_str)
    ints_str_sort = sorted(ints_str, key = cmp_to_key(suma))
    print(ints_str_sort)

    result = int(''.join(reversed(ints_str_sort))) - int(''.join(ints_str_sort))
    
    print(result)
    return result


# Best Solution:
# https://py.checkio.org/mission/bigger-together/publications/BeranekP/python-3/bigger-together-naive-approach/?ordering=most_voted&filtering=all

from itertools import permutations

def bigger_together(ints: List[int]) -> int:
    """
        Returns difference between the largest and smallest values
        that can be obtained by concatenating the integers together.
    """
    
    strs = [str(i) for i in ints]  # convert to strings
    print(strs)
    comb = permutations(strs, len(strs))  # find all possible combinations
    print(comb)
    nums = [int(''.join(c)) for c in comb]  # every comb -> join and convert to int  
    print(nums)
    
    return max(nums) - min(nums)


# Best Solution: 
# https://py.checkio.org/mission/bigger-together/publications/BeranekP/python-3/bigger-together-naive-approach/share/97fadc6f76a7e938f7d24ecadf7df96f/

from itertools import permutations

def bigger_together_(ints):
    """
        Returns difference between the largest and smallest values
        that can be obtained by concatenating the integers together.
    """
    strs = [str(i) for i in ints]  # convert to strings
    comb = permutations(strs, len(strs))  # find all possible combinations
    nums = [int(''.join(c)) for c in comb]  # every comb -> join and convert to int  
    
    return max(nums) - min(nums)


# Another Best Solution
# https://py.checkio.org/mission/bigger-together/publications/kurosawa4434/python-3/second/share/752a0b2fbf634c24bdd0431d666fe816/

from functools import cmp_to_key

def bigger_together_(ints):

    rs = sorted(map(str, ints), key=cmp_to_key(lambda a, b: int(a+b)-int(b+a)))

    return int(''.join(reversed(rs))) - int(''.join(rs))




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1,2,3,4]) == 3087, "4321 - 1234"
    assert bigger_together([1,2,3,4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print('Done! I feel like you good enough to click Check')