'https://py.checkio.org/en/mission/determinant/'

'''
In linear algebra, the determinant is a value associated with a square matrix. 
It can be computed from the entries of the matrix by a specific arithmetic expression (There are other ways to determine its value as well.)
'''

import numpy as np

def checkio(data):
    data_array = np.array(data)
    print(data_array)
    
    determinant = np.linalg.det(data_array)
    print(determinant)
    
    return determinant

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[4, 3], [6, 3]]) == -6, 'First example'

    assert checkio([[1, 3, 2],
                    [1, 1, 4],
                    [2, 2, 1]]) == 14, 'Second example'