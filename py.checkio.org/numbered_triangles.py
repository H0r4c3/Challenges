'https://py.checkio.org/en/mission/numbered-triangles/'

'''
You can move, rotate and flip the chips so they form a hexagon. 
The hexagon is only legal if the adjacent edges for each triangle have matching numbers.
'''
from collections import Counter

def checkio_(chips):
    #print(set(chips[0]).isdisjoint(chips[1]))
    
    # create a list with all lists that have common elements with chips[0]
    zero = [item for item in chips if not set(chips[0]).isdisjoint(item)]
    #print(zero)
    
    # create a list with all numbers
    all_numbers = sorted([item for sublist in chips for item in sublist])
    print(all_numbers)
    
    rep = Counter(all_numbers).most_common()
    print(rep)
        
    return 0


# Best Solution: https://py.checkio.org/mission/numbered-triangles/publications/Cjkjvfnby/python-3/__/share/e76426468b63e43acfcc6093d1efda3f/

from itertools import permutations

# triangle schema: start, end, val
def count_sum(block, triangles):
    start, end, val = block
    if not triangles:
        return val
    has_matches = (x for x in triangles if end in x)  # filter out not matching triangles
    result = []
    for match in has_matches:
        for tr_start, tr_end, tr_summ in permutations(match):
            if tr_start == end and (len(triangles) != 1 or  tr_end == start):
                new_triangles = list(triangles)
                new_triangles.remove(match)
                result.append(count_sum((start, tr_end, val + tr_summ), new_triangles))
    return len(result) and max(result)

def checkio(chips):
    first, *triangles = chips
    return max(count_sum(x, triangles) for x in permutations(first))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"