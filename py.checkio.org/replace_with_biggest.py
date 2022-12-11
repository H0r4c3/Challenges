'https://py.checkio.org/en/mission/replace-with-biggest/share/64fbafac0befc2c57ec63bfd02910221/'

'''
You are given a list of integers data. Replace every element in it with the biggest element 
among the elements to its strict right (not including current element). 
The last element should be replaced with -1. Return modified sequence as any Iterable.
'''

from typing import Iterable

def replace_biggest(data: list[int]) -> Iterable[int]:
    if data == []:
        return []
    
    for i in range(len(data) - 1):
        m = max(data[i+1 : ])
        data[i] = m
    
    data[-1] = -1
    
    print(data)    
    return data


print("Example:")
#print(list(replace_biggest([17, 18, 5, 4, 6, 1])))

# These "asserts" are used for self-checking
assert list(replace_biggest([17, 18, 5, 4, 6, 1])) == [18, 6, 6, 6, 1, -1]
assert list(replace_biggest([1, 2, 3, 4, 5, 6])) == [6, 6, 6, 6, 6, -1]
assert list(replace_biggest([1, 1, 1])) == [1, 1, -1]
assert list(replace_biggest([])) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")