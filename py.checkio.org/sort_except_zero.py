'https://py.checkio.org/en/mission/sort-except-zero/'

'''
Sort the numbers in an array. But the position of zeros should not be changed.
'''

from typing import Iterable


def except_zero(items: list) -> Iterable:
    enum0 = list()
    result = list()
    
    enum = list(enumerate(items))
    enum.sort(key=lambda x : x[1])
    
    for item in enum:
        if item[1] == 0:
            enum0.append(item)
        else:
            result.append(item[1])
    
    for item in enum0: 
        result.insert(item[0], item[1])
    
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]