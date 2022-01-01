'https://py.checkio.org/en/mission/can-pass/'

'''
You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value. The matrix consists of digits. 
You may move to neighboring cells either horizontally or vertically provided the values of the origin and destination cells are equal. 
You should determine if a path exists between two given cells.

A matrix is represented as a tuple of tuples with digits. Coordinates are represented as a tuple with two numbers: row and column. 
The result should be any value which can be converted into a boolean. If a path exists, then return True. Return False if there is none.

Input: Three arguments. A matrix as a tuple of tuples with integers, first and second cell coordinates as tuples of two integers.

Output: The existence of a path between two given cells as a boolean or a value that can be converted to boolean.

How it is used: Sometimes we don't need the full pathfinding algorithms implementation and can use simplified realization of these algorithms. 
It can be an useful skill to find a simple ways.
'''

from itertools import product

def can_pass(matrix, first, second):
    """
    Check if a path exists between first and second.
    """
    # create a set that contains all the cells with the same value as first
    valid = {(x,y) for x,y in product(range(len(matrix)), range(len(matrix[0]))) if matrix[x][y] == matrix[first[0]][first[1]]}
    current = {first}
    
    # if current is empty, path is dead. If second in current, path is found
    while current and second not in current:
        valid -= current     # remove current cells to prevent back tracking
        
        # find all cells in valid that are neighbors of any current cells
        # test for neighbor is abs(pt[0]-c_pt[0]) + abs(pt[1]-c_pt[1]) == 1
        current = {pt for pt in valid for c_pt in current if sum((abs(a-b) for a,b in zip(pt, c_pt))) == 1}
        
    return bool(current)


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'