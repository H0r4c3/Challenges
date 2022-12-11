'https://py.checkio.org/en/mission/move-zeros/'

'''
You are given a list of integers. Move all zeros in the list to the end of it. The order of non-zero elements should not change.
'''

from typing import Iterable

def move_zeros(items: list[int]) -> Iterable[int]:
    items_nonzero = [item for item in items if item != 0]
    result = items_nonzero + [0]*items.count(0)
    return result


print("Example:")
#print(list(move_zeros([0, 1, 0, 3, 12])))

# These "asserts" are used for self-checking
assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
assert list(move_zeros([0])) == [0]
assert list(move_zeros([0, 0, 0, 1, 2, 5, 6])) == [1, 2, 5, 6, 0, 0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")