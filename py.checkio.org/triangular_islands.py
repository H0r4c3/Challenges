'https://py.checkio.org/en/mission/triangular-islands/'

'''
The triangular sea area is divided into several triangular areas, numbered from top to bottom and from left to right in row-major order.

You are given a set of integers with land numbers as input values.

Triangles with adjacent sides are considered to be a group of the same island.
The number of those triangles is the island area.
You have to return a list (or an iterable) of the island areas you’ve found.
'''

# My Solution:

from typing import Set, Iterable
from math import sqrt, ceil

row_max = 0

def find_neighbors_row(my_list):
    '''find the neighbors of items in a list'''
    neighbors_row = dict()
    if len(my_list) == 1:
        return {my_list[0] : [my_list[0]]}
    for item in my_list:
        pos = my_list.index(item)
        if pos == 0:
            neighbors_row[item] = [my_list[pos+1]]
        elif pos == len(my_list) - 1:
            neighbors_row[item] = [my_list[pos-1]]
        else:
            neighbors_row[item] = [my_list[pos-1], my_list[pos+1]]        

    return neighbors_row

def find_neighbors_col(my_list, row, row_max):
    neighbors_col = dict()
    for item in my_list:
        pos = my_list.index(item)
        if pos % 2 == 0:
            neighbors_col[item] = [item + row*2] if row != row_max else []
        else:
            neighbors_col[item] = [item - (row-1)*2]
    
    return neighbors_col

def chain_common_elements(list_of_groups):
    '''
    Compare each set in a list with the rest of sets, and, if they have something in common, unite them
    '''
    for i in range(len(list_of_groups)-1):
        groups = list()
        for j in range(i+1, len(list_of_groups)):
            if not list_of_groups[i].isdisjoint(list_of_groups[j]):
                list_of_groups[i] = list_of_groups[i].union(list_of_groups[j])
                list_of_groups[j] = list_of_groups[i]

    list_of_groups = map(tuple, list_of_groups)
    groups = list(dict.fromkeys(list_of_groups))
    return groups


def triangular_islands(triangles: Set[int]) -> Iterable[int]:
    # find the total numbers of rows (row_max)
    max_nr = max(triangles)
    row_max = ceil(sqrt(max_nr))
    
    print(f'row_max = {row_max}')
    
    # make a dictionary with the numbers in rows
    # {1: [1], 2: [2, 3, 4], 3: [5, 6, 7, 8, 9], 4: [10, 11, 12, 13, 14, 16], 5: [17, 18, 19, 20, 21, 22, 23, 24, 25], 6: [26, 27, ..., 36]}
    #rows = {'row' + str(key) : [value for value in range((key-1)**2 + 1, key**2 + 1)] for key in range(1, 7)}
    rows = {key : [value for value in range((key-1)**2 + 1, key**2 + 1)] for key in range(1, row_max+1)}
    print(f'rows: \n {rows} \n')
    
    # make a list of list with the numbers in rows
    rows_list = [item for item in rows.values()]
    print(f'rows_list: \n {rows_list} \n')
    
    # make a dictionary with the neighbors in rows
    bors_row = dict()
    for item in rows_list:
        neighbors_row = find_neighbors_row(item)
        bors_row.update(neighbors_row)
    print(f'bors_row: \n {bors_row} \n')
    
    # make a dictionary with the neighbors in columns:
    bors_col = dict()
    for item in rows_list:
        row = rows_list.index(item) + 1
        neighbors_col = find_neighbors_col(item, row, row_max)
        bors_col.update(neighbors_col)
    print(f'bors_col: \n {bors_col} \n')
    
    # merge the dictionaries bors_row and bors_col = bors_all (all neighbors):
    bors_all = bors_row.copy()
    for v1, v2 in zip(bors_all.values(), bors_col.values()):
        v1.extend(v2)
        v1.sort()
    print(f'bors_all: \n {bors_all} \n')
    
    # find the neighbors of the numbers in triangles
    bors = {key : value for key, value in bors_all.items() if key in triangles}
    print(f'bors: \n {bors} \n') # {1: [1, 3], 4: [3, 8], 7: [6, 8], 8: [4, 7, 9]}
    
    if triangles == {1}:
        return [1]
    
    lands = list(bors.keys())
    print(f'lands = {lands}')
    bors_list = list(bors.values())
    print(f'bors_list = {bors_list}')
    
    # create a list of sets where every set is a land + neighbors of that land
    list_of_groups = list()
    result = list()
    for land in lands:
        n = {land}
        list_of_groups.append(n)
        for bor in bors_list:
            if land in bor:
                idx = bors_list.index(bor)
                n.add(lands[idx])
        
    print(f'list_of_groups: \n {list_of_groups} \n') # [{1}, {8, 4}, {8, 7}, {8, 4, 7}]
    
    # Unify the groups from list_of_groups in order to make the unique groups
    groups = chain_common_elements(list_of_groups)
    groups = list(map(sorted, groups))
    print(f'groups: \n = {groups} \n')
    print(sorted(triangles))
    
    groups_unique = list()
    for item in groups:
        if item not in groups_unique:
            groups_unique.append(item)
            
    print(f'groups_unique: \n = {groups_unique} \n')
    
    groups_unique2 = groups_unique.copy()
    for i in range(len(groups_unique)-1):
        groups = list()
        for j in range(i+1, len(groups_unique)):
            if set(groups_unique[i]).issuperset(set(groups_unique[j])):
                if groups_unique[j] in groups_unique2:
                    groups_unique2.remove(groups_unique[j])
            elif set(groups_unique[j]).issuperset(set(groups_unique[i])):
                if groups_unique[i] in groups_unique2:
                    groups_unique2.remove(groups_unique[i])
    
    
    # Make a list with the lengths of all groups
    result = list(map(lambda x: len(x), groups_unique2))
    result.sort()
    
    print(result)
    return result



# Best Solution: 
# https://github.com/kurosawa4434/checkio-mission-triangular-islands/blob/master/verification/my_solution.py

import bisect
from collections import defaultdict

def triangular_islands_(triangles):
    squars = []
    n = 1
    while True:
        if (sq := n ** 2) > 1000000:
            break
        squars.append(sq)
        n += 1

    adj_dict = dict()
    for t in triangles:
        bl = bisect.bisect_left(squars, t)

        if bl % 2 == t % 2:
            v = t - bl * 2
        else:
            v = t + (bl + 1) * 2
        adj_nums = [t - 1, v, t + 1]

        first = bl ** 2 + 1
        last = first + bl * 2

        if t == first:
            adj_nums = adj_nums[1:]
        if t == last:
            adj_nums = adj_nums[:-1]
        adj_dict[t] = set(adj_nums)

    colors = defaultdict(int)
    rest = set(triangles)

    def set_color(triangle, c):
        stack = [triangle]
        while stack:
            num = stack.pop()
            for r_num in list(rest):
                if r_num in adj_dict[num]:
                    colors[r_num] = c
                    stack.append(r_num)
                    rest.remove(r_num)

    c = 0
    for triangle in triangles:
        if not colors[triangle]:
            c += 1
            colors[triangle] = c
            set_color(triangle, c)

    t_groups = defaultdict(list)
    for k, v in colors.items():
        t_groups[v].append(k)

    return map(len, t_groups.values())



if __name__ == '__main__':
    print("Example:")
    #print(sorted(triangular_islands({1})))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sorted(triangular_islands({1, 4, 7, 8})) == [1, 3]
    assert sorted(triangular_islands({1})) == [1]
    assert sorted(triangular_islands({2, 3, 6})) == [3]
    assert sorted(triangular_islands({4, 3})) == [2]
    assert sorted(triangular_islands({1, 4, 7, 8})) == [1, 3]
    assert sorted(triangular_islands({1, 2, 3, 4, 5, 6, 7, 8, 9})) == [9]
    assert sorted(triangular_islands({1, 2, 4, 5, 7, 9})) == [1, 1, 1, 1, 1, 1]
    assert sorted(triangular_islands([20,32,25,8,46,24,40,6,44,18,41,7,29,33,10,23,39,19,43,47,30,11,36,48,17,45,2,49,4,26,16,12,1,3,27,5,38,14,21,28])) == [1,14,25]
    assert sorted(triangular_islands([10,20,2,36,6,29,18,7,21,3,13,34,30,19,22,26,8,23,17,31,28,16,9,5,12,15,24,32])) == [1,1,1,25]
    assert sorted(triangular_islands([10,100,39,69,58,9,70,75,73,35,99,28,61,88,66,85,51,2,14,55,60,41,27,96,81,53,97,4,8,37,76,93,77,29,47,79,17,30,32,3,49,22,59,16,36,82,63,18,72,57,89,11,5,56,19,24,43,90,33,71,34,64,65,54,67,45,74,52,1,15,62,12,7,68,38,25,42,91,86,46,84,13,95,44,78])) == [1,3,81]
    print("Coding complete? Click 'Check' to earn cool rewards!")