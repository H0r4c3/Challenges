'https://py.checkio.org/en/mission/rectangles-union/'

'''
Your mission is to calculate the area covered by a union of rectangles. 
The rectangles can have a non-empty intersection, which means that a simple sum of given rectangle areas doesn't work. 
Every rectangle is represented as 4 integers. 
The first two integers are the coordinates of a left-top corner, and the next two - of a bottom right corner.
'''

from typing import List, Tuple

def rectangles_union(recs: List[Tuple[int]]) -> int:
    rectangles = set()
    
    # add all rectangles with dimension 1x1 in a set
    for item in recs:
        x0, y0, x1, y1 = item
        for i in range(x0, x1): 
            for j in range(y0, y1):
                rectangles.add((i, j))
    
    print(rectangles)
    
    return len(rectangles)



# Best Solution: 
# https://py.checkio.org/mission/rectangles-union/publications/Merzix/python-3/1-liner/share/82d04ec0d378d6f355e95f40cb001e80/

from typing import List, Tuple

def rectangles_union_(recs: List[Tuple[int]]) -> int:
    return len({(i,j) for x0, y0, x1, y1 in recs for i in range(x0, x1) for j in range(y0, y1)})


if __name__ == '__main__':
    print("Example:")
    print(rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]) == 33
    assert rectangles_union([
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 19, 11),
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 16, 8)
    ]) == 0
    assert rectangles_union([
        
    ]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")