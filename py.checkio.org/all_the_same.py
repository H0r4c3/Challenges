'https://py.checkio.org/en/mission/all-the-same/'

'''
In this mission you should check if all elements in the given list are equal.
'''

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    elements_set = set(elements)
    
    if elements == [] or len(elements) == 1:
        return True
    elif len(elements_set) == 1:
        return True
    else:
        return False
    
    
# Best Solution:
# https://py.checkio.org/mission/all-the-same/publications/tom-tom/python-3/fifth/?ordering=most_voted&filtering=choice

def all_the_same(elements):
   return elements[1:] == elements[:-1]


if __name__ == '__main__':

    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True