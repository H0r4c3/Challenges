'https://py.checkio.org/en/mission/golden-pyramid/'

'''
Think of each step down to the left as moving to the same index location or to the right as one index location higher. 

Be very careful if you plan to use recursion here.

Input: A pyramid as a tuple of tuples. Each tuple contains integers.

Output: The maximum possible sum as an integer.
'''

# My Solution = ErrorTooLongForProcess!!!! (NOK)

from itertools import product

def replace_items_with_indices(my_list):
    '''Transform the pyramid into a pyramid of indices'''
    my_list_indices = [idx for idx, item in enumerate(my_list)]
    
    return my_list_indices


def check_neighbors(my_list):
    '''Verify that the next element in path is in range 1 from the previous one'''
    diff = [j-i for i, j in zip(my_list, my_list[1:])]
    
    return all(item == 0 or item == 1 for item in diff)


def convert_indices_in_values(path_indices, pyramid):
    '''Convert a path of indices into a path of values'''
    paths_values = list()
    for i in range(len(pyramid)):
        paths_values.append(pyramid[i][path_indices[i]])
    return paths_values


def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    
    # transform the pyramid in lists of indices
    pyramid_indices = list()
    for item in pyramid:
        pyramid_indices.append(replace_items_with_indices(item))
        
    print(pyramid_indices)
    
    # Brute Force: all combinations from lists of indices (all paths till down)
    prod = product(*pyramid_indices)
    #print(len(list(prod)))
    
    # only the paths with differences of indices == 0 or 1
    #paths = [item for item in prod if check_neighbors(item)]
    paths = filter(check_neighbors, prod)
    #print(len(list(paths)))
    #print(paths)
    
    # transform paths of indices into path of values
    paths_values = [convert_indices_in_values(path, pyramid) for path in list(paths)]
    print(paths_values)
    
    result = max(paths_values, key = lambda x : sum(x))
    
    print(result)
    return sum(result)


# Best Solution:
# https://py.checkio.org/mission/golden-pyramid/publications/zero_loss/python-3/first/?ordering=most_voted&filtering=all

def count_gold_(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    
    '''
    
    ===============
    Golden Pyramid
    ===============
    
    Approach
    --------
    
    This algorithm is a greedy approach to solving the problem.  
    Instead of working forward through the pyramid, we will work backwards.
    The idea is to start in the second to bottom row and select maxium of the
    the next two possible values from the current node and add that value to 
    the current node.
    
    After that we continue to roll up the rows and repeat the process for each
    node in that row.  When we reach the starting node we will have the sum
    of the maximum path.  
    
    *Note*: we are not finding the best path; we are only finding the maxium sum 
    from that path.  

    Code
    ----
    
    I want a mutable copy of the pyramid to work with.  
    Get the number of rows from the **len** function.  
    The last row is not in play to start hence **rows-1**
    Also we're working backwards so use the **reversed** function.
    Need to itertate over each item in the row. Note the plus 1, range(0) 
    returns an empty list.
    The possible nodes to examine are 1) the on directly below i+1,j
    and the one below and to the right i+1, j+1.  We use the **max** 
    function to select the largest one and then add it to the current
    node.  
    
    '''
    py = [list(i) for i in pyramid]
    for i in reversed(range(len(py)-1)):   
        for j in range(i+1):
            py[i][j] +=(max(py[i+1][j], py[i+1][j+1]))

    return py[0][0]



# Best Solution:
# https://py.checkio.org/mission/golden-pyramid/publications/chunshar/python-3/first/share/c79f52d96c22b64fb0e1a42c82977061/

def count_gold_(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    pyramid = [list(t) for t in pyramid]
    for y in range(1, len(pyramid)):
        for x in range(len(pyramid[y])):
            l = 0 if x == 0 else pyramid[y - 1][x - 1]
            r = 0 if x >= len(pyramid[y - 1]) else pyramid[y - 1][x]
            pyramid[y][x] += max(l, r)
    return max(pyramid[-1])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert count_gold((
    #     (1,),
    #     (2, 3),
    #     (3, 3, 1),
    #     (3, 1, 5, 4),
    #     (3, 1, 3, 1, 3),
    #     (2, 2, 2, 2, 2, 2),
    #     (5, 6, 4, 5, 6, 4, 3))) == 23, "First example"
    # assert count_gold((
    #     (1,),
    #     (2, 1),
    #     (1, 2, 1),
    #     (1, 2, 1, 1),
    #     (1, 2, 1, 1, 1),
    #     (1, 2, 1, 1, 1, 1),
    #     (1, 2, 1, 1, 1, 1, 9))) == 15, "Second example"
    # assert count_gold((
    #     (9,),
    #     (2, 2),
    #     (3, 3, 3),
    #     (4, 4, 4, 4))) == 18, "Third example"
    
    assert count_gold((
        (2,),
        (7,9),
        (0,8,6),
        (4,7,6,8),
        (0,5,5,4,1),
        (9,1,0,1,6,9))) == 35
    
    print('Done!!!')