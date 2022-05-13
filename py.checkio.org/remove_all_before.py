'https://py.checkio.org/en/mission/remove-all-before/'

'''
What you need to do here is to remove from the list all of the elements before the given one.
'''

from typing import Iterable

# My First Solution
def remove_all_before_(items: list, border: int) -> Iterable:
    # your code here
    if items == []:
        return items
    if border not in items:
        return items
    index = items.index(border)
    items = items[index:]
    return items


# My Second Solution (for using zip_longest quest)
from itertools import zip_longest
def remove_all_before(items: list, border: int) -> Iterable:
    if border not in items:
        return items
    
    result = list()
    
    i = len(items) - items.index(border)
    print(i)
    
    items1 = items[::-1]
    print(items1)
    
    border_list = i * [border]
    print(border_list)
    z = zip_longest(items1, border_list)
    #print(list(z))
    
    for item in list(z):
        print(item)
        if item[1] != None:
            result.append(item[0])
    
    print(f'result = {result[::-1]}')
    return result[::-1]
    
    
    
    

if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    assert list(remove_all_before([10,1,5,6,7,10],5)) == [5,6,7,10]
    print("Coding complete? Click 'Check' to earn cool rewards!")