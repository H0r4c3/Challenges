'https://py.checkio.org/en/mission/count-neighbours/share/4fb316bf2e2bb809a8252d9c911b492b/'

'''
Input: Three arguments:

A grid as a tuple of tuples containing integers 1 or 0)
A row number for a cell, as an integer
A column number for a cell, as an integer
Output: The number of neighbouring cells that have chips, as an integer.
'''
import numpy as np

def find_neighbors_coordinates(matrix, row, col):
    '''Find the <neighbors_coordinates> of neighbors for an element having <element_coordinates> in a <matrix>'''
    
    neighbors_coordinates = list()
    dimensions = matrix.shape
    
    x, y = row, col
    
    # coordinates horizontally and vertically 
    c1 = (x+1, y) if x+1 <= dimensions[0] - 1 else None
    c2 = (x, y+1) if y+1 <= dimensions[1] - 1 else None
    c3 = (x-1, y) if x-1 >= 0 else None
    c4 = (x, y-1) if y-1 >= 0 else None
    print(c1, c2, c3, c4)
    
    # coordinates diagonally
    c5 = (x-1, y-1) if (x-1 >= 0 and y-1 >= 0) else None
    c6 = (x-1, y+1) if (x-1 >= 0 and y+1 <= dimensions[1] - 1) else None
    c7 = (x+1, y-1) if (x+1 <= dimensions[1] - 1 and y-1 >= 0) else None
    c8 = (x+1, y+1) if (x+1 <= dimensions[1] - 1 and y+1 <= dimensions[1] - 1) else None
    
    neighbors_coordinates = [item for item in [c1, c2, c3, c4, c5, c6, c7, c8] if item != None]

    return neighbors_coordinates

def count_neighbours(grid, row, col):
    neighbors = list()
    matrix = np.array(grid)
    print(matrix)
    
    neighbors_coordinates = find_neighbors_coordinates(matrix, row, col)
    print(neighbors_coordinates)
    
    for item in neighbors_coordinates:
        neighbors.append(matrix[item])
    print(neighbors)
    
    print(neighbors.count(1))
    return neighbors.count(1)


# Best Solution: https://py.checkio.org/mission/count-neighbours/publications/shuai/python-3/second/?ordering=most_voted&filtering=all

def count_neighbours_(grid, row, col):
    num_row, num_col = len(grid), len(grid[1])
    neighbors = ((row-1, col-1), (row-1, col), (row-1, col+1),
                 (row, col-1), (row, col+1),
                 (row+1, col-1), (row+1, col), (row+1, col+1))
    return sum(0 <= i < num_row and 0 <= j < num_col and grid[i][j]
                for i, j in neighbors)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
    
    print('Done!')