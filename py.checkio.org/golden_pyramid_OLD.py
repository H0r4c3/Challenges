'https://py.checkio.org/en/mission/golden-pyramid/'

'''
Think of each step down to the left as moving to the same index location or to the right as one index location higher. 

Be very careful if you plan to use recursion here.

Input: A pyramid as a tuple of tuples. Each tuple contains integers.

Output: The maximum possible sum as an integer.
'''

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
        
    #print(pyramid_indices)
    
    # Brute Force: all combinations from lists of indices (all paths till down)
    prod = product(*pyramid_indices)
    
    # only the paths with differences of indices == 0 or 1
    paths = [item for item in prod if check_neighbors(item)]
    print(len(paths))
    print(paths)
    
    # transform paths of indices into path of values
    paths_values = [convert_indices_in_values(path, pyramid) for path in paths]
    paths_values = sorted(paths_values, key = lambda x : sum(x), reverse=True)
    print(paths_values[0])
    
    print(sum(paths_values[0]))
    return sum(paths_values[0])


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