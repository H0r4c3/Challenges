'https://py.checkio.org/en/mission/chunk/'

'''
Split a list into smaller lists of the same size (chunks). 
The last chunk can be smaller than the default chunk-size. If the list is empty, then you shouldn't have any chunks at all.
'''

from typing import Iterable

def chunking_by(items: list, size: int) -> Iterable:
    result = [items[i : i+size] for i in range(0, len(items), size)]
    
    print(result)
    return result

    


if __name__ == '__main__':
    print("Example:")
    print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
    print("Coding complete? Click 'Check' to earn cool rewards!")