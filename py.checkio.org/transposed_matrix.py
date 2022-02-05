'https://py.checkio.org/en/mission/matrix-transpose/'

'''
In linear algebra, the transpose of a matrix A is another matrix A T (also written A ′, A tr , t A or A t ) 
created by any one of the following equivalent actions:

reflect A over its main diagonal (which runs from top-left to bottom-right) to obtain A T
write the rows of A as the columns of A T
write the columns of A as the rows of A T
'''

from typing import List
import numpy as np
def checkio(data: List[List[int]]) -> List[List[int]]:
    transpose_data = [list(i) for i in np.transpose(data)]
    
    print(transpose_data)
    return transpose_data


# 2. Solution
def checkio_(data: List[List[int]]) -> List[List[int]]:
    transpose_data = [list(i) for i in zip(*data)]
    
    print(transpose_data)
    return(transpose_data)


# 3. Solution
def checkio_(data: List[List[int]]) -> List[List[int]]:
    transpose_data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    
    print(list(transpose_data))
    return(list(transpose_data))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]))

    assert isinstance(checkio([[0]]).pop(), list) is True, "Match types"
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"
    print("Coding complete? Click 'Check' to earn cool rewards!")