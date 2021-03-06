'https://py.checkio.org/en/mission/split-list/'

'''
You have to split a given array into two arrays. 
If it has an odd amount of elements, then the first array should have more elements. 
If it has no elements, then two empty arrays should be returned.
'''

def split_list_(items: list) -> list:
    result = list()
    
    if items == []:
        return [[],[]]
    
    length = len(items)
    
    if length % 2 == 0:
        list1 = items[ : length // 2]
        list2 = items[length // 2  : ]
        result.append(list1)
        result.append(list2)
        
        return result
    
    if length % 2 != 0:
        list1 = items[ : length // 2 + 1]
        list2 = items[length // 2 + 1 : ]
        result.append(list1)
        result.append(list2)
        
        return result
    

# Best Solution: 
# https://py.checkio.org/mission/split-list/publications/Roman_13/python-3/first/?ordering=most_voted&filtering=all

import numpy as np

def split_list(items: list) -> list:
    
    return np.array_split(items,2)


if __name__ == '__main__':
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]