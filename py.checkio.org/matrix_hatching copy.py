'https://py.checkio.org/en/mission/matrix-hatching/share/3e47b57d96b84215634862349b262b47/'

'''
You are given a 2-dimensional matrix: a list of lists of integers. 
Your function should return another Iterable of lists, 
where each inner list is a sequence of matrix elements on the same diagonal "stroke". 
The order of elements in the "stroke" is SW -> NE.
'''

import numpy as np
from typing import Iterable


def hatching_(matrix: list[list[int]]) -> Iterable[list[int]]:
    matrix_arr = np.array(matrix)
    print(matrix_arr)
    
    # main diagonal
    print(np.diag(matrix_arr, k=0))
    
    # above main diagonal
    print(np.diag(matrix_arr, k=1))
    
    # below main diagonal
    print(np.diag(matrix_arr, k=-1))
    
    return [[]]


def hatch_cols(r, c, arr):
    ''' r < c'''
    # 2 x 5
    result = [[] for _ in range(6)]
    r, c = 0, 0
    result[0] = arr[r, c]
    result[1] = [arr[r+1, c],   arr[r, c+1]]
    result[2] = [arr[r+1, c+1], arr[r, c+2]]
    result[3] = [arr[r+1, c+2], arr[r, c+3]]
    result[4] = [arr[r+1, c+3], arr[r, c+4]]
    result[5] = [arr[r+1, c+4]]
    
    return result

def hatch_rows(r, c, arr):
    ''' r > c'''
    # 5 x 2
    result = [[] for _ in range(6)]
    r, c = 0, 0
    result[0] = arr[r, c]
    result[1] = [arr[r+1, c],   arr[r, c+1]]
    result[2] = [arr[r+2, c],   arr[r+1, c+1]]
    result[3] = [arr[r+3, c],   arr[r+2, c+1]]
    result[4] = [arr[r+4, c],   arr[r+3, c+1]]
    result[5] = [arr[r+4, c+1]]
    
    return result

def hatch_square(r, c, arr):
    ''' r == c'''
    # 3 x 3
    result = [[] for _ in range(5)]
    r, c = 0, 0
    result[0] = arr[r, c]
    result[1] = [arr[r+1, c],   arr[r, c+1]]
    result[2] = [arr[r+2, c],   arr[r+1, c+1], arr[r, c+2]]
    result[3] = [arr[r+2, c+1], arr[r+1, c+2]]
    result[4] = [arr[r+2, c+2]]
    
    return result

def hatching(matrix: list[list[int]]) -> Iterable[list[int]]:
    r = len(matrix)
    c = len(matrix[0])
    print(r, c)
    
    arr = np.array(matrix)
    print(arr)
    
    if r < c:
        result = hatch_cols(r, c, arr)
    
    elif r > c:
        result = hatch_rows(r, c, arr)
    
    # r == c    
    else:
        result = hatch_square(r, c, arr)
        
    print(result)
    return result


print("Example:")
#print(list(hatching([[1, 2], [3, 4]])))

# These "asserts" are used for self-checking
assert list(hatching([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])) == [[1], [4, 2], [7, 5, 3], [8, 6], [9]]
#assert list(hatching([[0]])) == [[0]]
#assert list(hatching([[1, 2], [3, 4]])) == [[1], [3, 2], [4]]
assert list(hatching([[1, 2, 3, 4, 5], 
                      [6, 7, 8, 9, 0]])) == [
    [1],
    [6, 2],
    [7, 3],
    [8, 4],
    [9, 5],
    [0],
]
assert list(hatching([[1, 2], 
                      [3, 4], 
                      [5, 6], 
                      [7, 8], 
                      [9, 0]])) == [
    [1],
    [3, 2],
    [5, 4],
    [7, 6],
    [9, 8],
    [0],
]

print("The mission is done! Click 'Check Solution' to earn rewards!")