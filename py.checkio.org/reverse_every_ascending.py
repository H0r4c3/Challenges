'https://py.checkio.org/en/mission/reverse-every-ascending/'

'''
Create and return a new iterable that contains the same elements as the argument iterable items, but with the reversed order of the elements inside every maximal strictly ascending sublist. This function should not modify the contents of the original iterable.

Input: Iterable

Output: Iterable

reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
'''

import numpy as np

def reverse_ascending(items):
    new_list = list()
    
    result = np.split(items, np.where(np.diff(items) <= 0)[0] + 1)
    
    for item in result:
        new_list.extend(sorted(list(item), reverse=True))
    
    #print(new_list)
    return new_list


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]