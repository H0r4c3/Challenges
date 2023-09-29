'https://py.checkio.org/en/mission/connect-stars/'

'''
You are given a list of coordinates of vertices. Each coordinate is a tuple of x (integer) and y (integer).
You have to return a list (or an iterable) of lines that connect all vertices. 
The total length of lines should be the minimum. Each line is a tuple of two integers. 
These integers represent the index of list of input.
'''

from typing import List, Tuple, Iterable


import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

def connect_stars(coords):
    '''
    distance_matrix = Returns the matrix of all pair-wise distances
    
    Matrix containing the distance from every vector in x to every vector in y.
    '''
    dist_mat = distance_matrix(coords, coords)
    print(dist_mat)
    
    '''
    minimum_spanning_tree = Return a minimum spanning tree of an undirected graph. 
    
    A minimum spanning tree is a graph consisting of the subset of edges which together 
    connect all connected nodes, while minimizing the total sum of weights on the edges.
    '''
    min_span_tree = minimum_spanning_tree(dist_mat)
    print(min_span_tree)
    
    '''
    argwhere = Find the indices of array elements that are non-zero, grouped by element.
    Indices of elements that are non-zero. Indices are grouped by element. 
    This array will have shape (N, a.ndim) where N is the number of non-zero items.
    '''
    index_array = np.argwhere(min_span_tree != 0).tolist()
    print(index_array)
    
    return index_array


if __name__ == '__main__':

    print("Example:")
    print(connect_stars([(1, 1), (4, 4)]))

    def sort_edges(edges): return sorted(map(lambda e: tuple(sorted(e)), edges))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_edges(connect_stars([(1, 1), (4, 4)])) == [(0, 1)], '2 vertices'
    assert sort_edges(connect_stars([(1, 1), (4, 1), (4, 4)])) == [(0, 1), (1, 2)], '3 vertices'
    assert sort_edges(connect_stars([(6, 6), (6, 8), (8, 4), (3, 2)])) == [(0, 1), (0, 2), (0, 3)], '4 vertices'
    assert sort_edges(connect_stars([(5, 4), (5, 1), (2, 6), (7, 2), (6, 9)])) == [(0, 2), (0, 3), (1, 3), (2, 4)], '5 vertices'
    assert sort_edges(connect_stars([(5, 8), (5, 1), (4, 2), (7, 6), (8, 6), (2, 2)])) == [(0, 3), (1, 2), (2, 3), (2, 5), (3, 4)], '6 vertices'
    assert sort_edges(connect_stars([(2, 7), (9, 9), (4, 9), (9, 6), (3, 3), (1, 6), (9, 7)])) == [(0, 2), (0, 5), (1, 2), (1, 6), (3, 6), (4, 5)], '7 vertices'
    print("Coding complete? Click 'Check' to earn cool rewards!")