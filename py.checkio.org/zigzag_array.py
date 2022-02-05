'https://py.checkio.org/en/mission/zigzag-array/'

'''
This function creates an List of lists. that represents a two-dimensional grid with the given number of rows and cols. 
This grid should contain the integers from start to start + rows * cols - 1 in ascending order, but the elements of 
every odd-numbered row have to be listed in descending order, so that when read in ascending order, the numbers zigzag through the two-dimensional grid.
'''

from typing import List

def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    numbers = list(range(start, (start + rows*cols)))
    print(numbers)
    
    if cols == 0:
        return [[] for _ in range(rows)]
        
    numbers_sliced = [list(numbers[i : i + cols]) for i in range(0, rows*cols, cols)]
    print(numbers_sliced)
    zigzag = [item[::-1] if (numbers_sliced.index(item) % 2) else item for item in numbers_sliced]
    print(zigzag)
    
    return zigzag


# Best solution: https://py.checkio.org/mission/zigzag-array/publications/veky/python-3/and-thats-how-you-use-islice/?ordering=most_voted&filtering=all

from typing import List
from itertools import count, islice

def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    it = count(start)
    return [list(islice(it, cols))[::(-1)**row] for row in range(rows)]


if __name__ == '__main__':
    print("Example:")
    #print(create_zigzag(3, 3, 5))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert create_zigzag(3, 5) == [
        [1,2,3,4,5],
        [10,9,8,7,6],
        [11,12,13,14,15]
    ]
    assert create_zigzag(5, 1) == [
        [1],
        [2],
        [3],
        [4],
        [5]
    ]
    assert create_zigzag(3, 3, 5) == [
        [5, 6, 7],
        [10, 9, 8],
        [11, 12, 13]
    ]

    # Edge cases
    assert create_zigzag(0, 3) == []
    assert create_zigzag(3, 0) == [[], [], []]
    assert create_zigzag(0, 0) == []

    print("Coding complete? Click 'Check' to earn cool rewards!")