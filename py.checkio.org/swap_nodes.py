'https://py.checkio.org/en/mission/swap-nodes/'

'''
Your task is to swap elements of the list (Iterable) pairwise. If you are given a list of 4 elements, 
then your function should return the same list, only in it the first and second elements are interchanged, as well as the third and fourth.

If there isn’t a paired amount of elements, then leave the last unpaired element in its place. An empty list should remain empty.
'''
from itertools import pairwise, chain

def swap_nodes(a):
    pair_a = list(pairwise(a))
    print(pair_a)
    
    pair_a_ok = [(item[1], item[0]) for idx, item in enumerate(pair_a) if idx % 2 == 0]
    print(f'pair_a_ok = {pair_a_ok}')
    
    result = list(chain.from_iterable(pair_a_ok))
    
    if len(a) % 2 == 0:
        return result
    else:
        result.append(a[-1])
        return result
    
# Best Solutions: 
# https://py.checkio.org/mission/swap-nodes/publications/rodka81/python-3/plain-and-simple/?ordering=most_voted&filtering=all

def swap_nodes(a):
    for i in range(0, len(a)-1, 2):
        a[i], a[i+1] = a[i+1], a[i]
    return a


# https://py.checkio.org/mission/swap-nodes/publications/Sim0000/python-3/iter/?ordering=most_voted&filtering=all

from itertools import zip_longest

def swap_nodes(a):
    it = iter(a)
    for x, y in zip_longest(it, it):
        if y: yield y
        yield x


if __name__ == '__main__':
    print("Example:")
    #print(list(swap_nodes([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert list(swap_nodes([1, 2, 3, 4])) == [2, 1, 4, 3]
    assert list(swap_nodes([5, 5, 5, 5])) == [5, 5, 5, 5]
    assert list(swap_nodes([1, 2, 3])) == [2, 1, 3]
    assert list(swap_nodes([3])) == [3]
    assert list(swap_nodes(["hello", "world"])) == ["world", "hello"]
    print("Coding complete? Click 'Check' to earn cool rewards!")