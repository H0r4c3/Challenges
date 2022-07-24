'https://py.checkio.org/en/mission/find-sequence/'

'''
You are given a matrix of NxN (4≤N≤10). 
You should check if there is a sequence of 4 or more matching digits. 
The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
'''

import numpy as np
from itertools import groupby
from typing import List

def check_consecutives(my_list):
    result = any(sum(1 for _ in rep) >= 4 for _, rep in groupby(my_list))
    return result

def checkio_(matrix: List[List[int]]) -> bool:
    matrix_arr = np.array(matrix)
    
    # rows
    for row in matrix_arr:
        if check_consecutives(row):
            return True
    
    # columns    
    for i in range(len(matrix[0])):
        if check_consecutives(matrix_arr[:,i]):
            return True
    
    # diagonals
    #diag1 = matrix_arr.diagonal(0, 0, 1)
    for i in range(len(matrix[0])):
        if check_consecutives(matrix_arr.diagonal(i, 0, 1)):
            return True
    
    #diag2 = np.fliplr(matrix_arr).diagonal(0, 1, 0)
    for i in range(len(matrix[0])):
        if check_consecutives(matrix_arr.diagonal(i, 1, 0)):
            return True
    
    return False


def checkio(matrix: List[List[int]]) -> bool:
    matrix_arr = np.array(matrix)
    
    all_lists = list()
    
    # rows
    rows = list()
    for row in matrix_arr:
        rows.append(list(row))
    print(f'rows = {rows} \n')
    
    # columns  
    columns = list()  
    for i in range(len(matrix[0])):
        columns.append(list(matrix_arr[:,i]))
    print(f'columns = {columns} \n')
    
    # diagonals
    diagonals_1_up = list()
    for i in range(len(matrix[0])):
        diagonals_1_up.append(list(matrix_arr.diagonal(i, 0, 1)))
    print(f'diagonals_1_up = {diagonals_1_up} \n')
    
    diagonals_1_down = list()
    for i in range(len(matrix[0])):
        diagonals_1_down.append(list(matrix_arr.diagonal(i, 1, 0)))
    print(f'diagonals_1_down = {diagonals_1_down} \n')
    
    
    matrix_fliplr = np.fliplr(matrix_arr)
    
    diagonals_2_up = list()
    for i in range(len(matrix[0])):
        diagonals_2_up.append(list(matrix_fliplr.diagonal(i, 0, 1)))
    print(f'diagonals_2_up = {diagonals_2_up} \n')
    
    diagonals_2_down = list()
    for i in range(len(matrix[0])):
        diagonals_2_down.append(list(matrix_fliplr.diagonal(i, 1, 0)))
    print(f'diagonals_2_down = {diagonals_2_down} \n')
    
    for item in [rows, columns, diagonals_1_up, diagonals_1_down, diagonals_2_up, diagonals_2_down]:
        all_lists.extend(item)
    print(f'all_lists = {all_lists} \n')
    
    for item in all_lists:
        if check_consecutives(item):
            return True
    else:
        return False
    
    
    
# Best Solution: 
# https://py.checkio.org/mission/find-sequence/publications/Phil15/python-3/with-chain-rowscolsdiags-generators/?ordering=most_voted&filtering=all

from itertools import chain

def checkio_(matrix):
    """Generate rows, columns, descending and ascending diagonals.
    Then for each line, we look for 4 egals consecutives elements."""
    check = lambda line: any(line[i]==line[i+1]==line[i+2]==line[i+3]
                             for i in range(len(line)-3))
    N = len(matrix)
    rows = (mat for mat in matrix)
    cols = ([mat[j] for mat in matrix] for j in range(N))
    d_diag = ([mat[i+k] for i,mat in enumerate(matrix) if 0<=i+k<N]
              for k in range(-(N-4),N-4+1))
    a_diag = ([mat[N-1-i+k] for i,mat in enumerate(matrix) if 0<=N-1-i+k<N]
              for k in range(-(N-4),N-4+1))
    return any(check(line) for line in chain(rows, cols, d_diag, a_diag))



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    assert checkio([[2,6,2,3,5,2,4,8,7],
                    [5,7,8,5,9,5,7,3,4],
                    [6,4,1,2,1,6,5,8,5],
                    [9,3,1,3,5,4,6,4,8],
                    [9,6,6,8,1,9,1,2,1],
                    [5,5,5,8,6,5,3,2,5],
                    [7,5,2,9,2,9,8,2,5],
                    [5,8,1,9,1,2,6,2,2],
                    [7,5,3,6,1,6,9,5,9]])
    
    print('All Done! Time to check!')