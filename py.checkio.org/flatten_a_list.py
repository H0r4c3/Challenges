'https://py.checkio.org/en/mission/flatten-list/'

'''
There is a list which contains integers or other nested lists which may contain yet more lists and integers which then… you get the idea. 
You should put all of the integer values into one flat list. The order should be as it was in the original list with string representation from left to right.

We need to hide this program from Nikola by keeping it small and easy to hide. Because of this, your code should be shorter than 140 characters (with whitespaces) .

Input data: A nested list with integers.

Output data: The one-dimensional list with integers.
'''

# 1. Solution
from pandas.core.common import flatten
def flat_list(array):
    return list(flatten(array))



# 2. Solution
from itertools import chain
from collections.abc import Iterable
def flat_list_(array):
    
    def flat(array):
        result = list()
        for item in array:
            if isinstance(item, Iterable):
                c = list(chain(item))
                result.extend(c)
            else:
                result.append(item)
                
        print(result)
        return result
            
    while any(isinstance(item, Iterable) for item in array):
        array = flat(array)
    
    return array



# Best 'Speedy' Solution for Flatten a List (iterator version):
# https://py.checkio.org/en/mission/flatten-a-list-iterator-version/

from collections.abc import Iterable
def flat_list_(array):
    for i in array:
        if isinstance(i, Iterable):
            yield from flat_list(i)
        else:
            yield i



# Best 'Speedy' Solution for Flatten a List:
# https://py.checkio.org/mission/flatten-list/publications/pavlik/python-3/flatten-a-list/?ordering=most_voted&filtering=all

def flat_list_(array):
    import re
    return [int(i) for i in re.findall(r'[-]?\d+', str(array))]



if __name__ == '__main__':
    #assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    #assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')