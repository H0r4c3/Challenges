'https://py.checkio.org/en/mission/similar-triangles/'

'''
This is a mission to check the similarity of two triangles.

You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

Input:

Two lists as coordinates of vertices of each triangle.
Coordinates is three tuples of two integers.
Output: True or False.
'''

from typing import List, Tuple
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    
    sides1 = sorted([((coords_1[i][0] - coords_1[i-1][0])**2 + (coords_1[i][1] - coords_1[i-1][1])**2)**0.5 for i in range(3)])
    
    sides2 = sorted([((coords_2[i][0] - coords_2[i-1][0])**2 + (coords_2[i][1] - coords_2[i-1][1])**2)**0.5 for i in range(3)])
    
    proportions = [sides1[i]/sides2[i] for i in range(3)]
    
    if len(set(proportions)) == 1:
        return True
    else:
        return False


    


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))
    print(similar_triangles([[1,3], [4,2], [2,1]], [[-1,-1], [2,-2], [0,-3]]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'