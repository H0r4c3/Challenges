'https://py.checkio.org/en/mission/shorter-set/share/cf9d0296628c4f791c44aab625069a56/'

'https://py.checkio.org/profile/leaderboard/all/2021/11/1/'

'''
In a given set of integers, you need to remove minimum and maximum elements.

The second argument tells how many min and max elements should be removed.

Input: Two arguments. Set of ints and int.

Output: Set of ints
'''

def remove_min_max(data: set, total:int) -> set:
    list_sorted = sorted(list(data))
    list_sliced = list_sorted[total : len(list_sorted) - total]
    
    return set(list_sliced)


print('Example:')
print(remove_min_max({4,5,6,7}, 1))

assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()