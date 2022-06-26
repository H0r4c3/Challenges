'https://py.checkio.org/en/mission/the-buttons/'

'''
There were buttons on the ceiling in the form of geometrical figures with written numbers on them. 
Your task is to press them in the correct order - starting from the most "valuable" and finishing with the least "valuable" one. 
The figure’s value corresponds with the sum of all the numbers on it. 
A separate geometrical figure is the one whose elements are directly connected to one another (horizontally or vertically). 
Your function should return a list where the values ​​of all figures will be listed in the order in which they should be pressed. 
0 is a symbol for separating the individual figures. If several figures have the same value, they can be pressed in any order.
'''

# NOK !!!!
import numpy as np

def buttons(ceiling):
    ceil_list = ceiling.splitlines()[1:]
    ceil = [list(map(int, item)) for item in ceil_list]
    ceil_arr = np.array(ceil)
    print(ceil_arr)
    print(ceil_arr.nonzero())
    
    positions = list(map(tuple, np.argwhere(ceil_arr>0).tolist()))
    print(positions)
    
    # create a dictionary having keys = rows, values = columns
    def create_dict(keys, values):
        rows_columns = dict()
        c, x, y = 0, 0, 0
        
        for key in set(keys):
            c = list(keys).count(key)
            y += c 
            rows_columns[key] = list(values)[x : y]
            x += c
        
        return rows_columns
    
    keys, values = ceil_arr.nonzero()
    
    # same as positions
    x = zip(keys, values)
    #print(keys, values)
    print(list(x))   
    
    #print(create_dict(keys, values))
    
    
    
    return 0



# Best Solution: 
# https://py.checkio.org/mission/the-buttons/publications/Merzix/python-3/8-liner/?ordering=most_voted&filtering=all

def buttons(ceiling):
    ceiling = [list(map(int, x)) for x in ceiling.splitlines()[1:]]
    max_h, max_w = len(ceiling) - 1, len(ceiling[0]) - 1
    
    def sum_around(h, w):
        if h < 0 or h > max_h or w < 0 or w > max_w or not ceiling[h][w]: return 0
        temp, ceiling[h][w] = ceiling[h][w], 0
        return temp + sum(sum_around(h + i, w + j) for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)])
    
    return sorted(filter(bool, [sum_around(x, y) for x in range(max_h + 1) for y in range(max_w + 1)]), reverse=True)


# Best Solution: 
# https://py.checkio.org/mission/the-buttons/publications/rodka81/python-3/compact-solution-with-numpy-and-scipyndimage/

import numpy as np
from scipy.ndimage import label

def buttons(ceiling):
    m = np.asarray([list(x) for x in ceiling.splitlines() if x]).astype(int)
    labeled_array, num_features = label(m)
    return sorted([np.asscalar(np.sum(m[labeled_array == i])) 
                  for i in range(1, num_features+1)], reverse=True)



if __name__ == '__main__':
    print("Example:")
    print(buttons('''
001203
023001
100220'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert buttons('''
001203
023001
100220''') == [8, 4, 4, 1]

    assert buttons('''
000000
000055
000055''') == [20]

    assert buttons('''
908070
060504
302010''') == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")