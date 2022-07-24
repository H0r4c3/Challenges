'https://py.checkio.org/en/mission/break-rings/'

'''
All of the rings are numbered and you are told which of the rings are connected. 
This information is given as a sequence of sets. Each set describes the connected rings.

Input: Information about the connected rings as a tuple of sets with integers.

Output: The number of rings to break as an integer.
'''

from itertools import product

def break_rings(rings):
    pr = product(*rings)
    pr_set = map(set, pr)
    pr_len = map(len, pr_set)

    return min(pr_len)



# Best Solution:
# https://py.checkio.org/mission/break-rings/publications/Sim0000/python-3/combination/?ordering=most_voted&filtering=all

from itertools import combinations

def break_rings_(rings):
    uniq_rings = set.union(*rings)
    for n in range(1, len(uniq_rings)):
        for destroy in combinations(uniq_rings, n): # we break n rings
            if all(ring & set(destroy) for ring in rings): return n # found
            
            
# Best Solution:
# https://py.checkio.org/mission/break-rings/publications/veky/python-3/obvious/?ordering=most_voted&filtering=all

from itertools import product
break_rings_ = lambda rings: min(len(set(cuts)) for cuts in product(*rings))


# Best Solution:
# https://py.checkio.org/mission/break-rings/publications/gyahun_dash/python-3/first/?ordering=most_voted&filtering=all

from itertools import product

def break_rings_(rings):
    return min(map(len, map(set, product(*rings))))



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    print('Done!!!')