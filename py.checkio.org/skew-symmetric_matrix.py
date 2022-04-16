'https://py.checkio.org/en/mission/skew-symmetric-matrix/'

'''
In mathematics, particularly in linear algebra, a skew-symmetric matrix (also known as an antisymmetric or antimetric) is 
a square matrix A which is transposed and negative. This means that it satisfies the equation A = −A T . 
https://en.wikipedia.org/wiki/Skew-symmetric_matrix

If the entry in the i-th row and j-th column is a ij , i.e. A = (a ij ) then the symmetric condition becomes a ij = −a ji .

You should determine whether the specified square matrix is skew-symmetric or not.
'''

# My Solution:

import numpy as np

def checkio(matrix):
    matrix_t = np.array(matrix).transpose()
    
    return (np.array(matrix) == -matrix_t).all()


# Another Solution: 
# https://py.checkio.org/mission/skew-symmetric-matrix/publications/OrginalS/python-3/first/?ordering=most_voted&filtering=all

def checkio(matrix):
    for i in range((len(matrix))):
        for j in range(i, len(matrix)):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]))

    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!");