'https://py.checkio.org/en/mission/when-k-is-enough/share/08f9b72785ad549e0c367f9196d1aff7/'

'''
Given a list of items, some of which may be duplicated, 
create and return a new Iterable that is otherwise the same as items, 
but only up to k occurrences of each element are kept, 
and all occurrences of that element after those first k are discarded. 
'''

from typing import Iterable


def remove_after_kth(items: list, k: int) -> Iterable:
    if k == 0:
        return []
    
    for item in items:
        repetitions = items.count(item)
        if repetitions > k:
            for _ in range (repetitions - k):
                items == items.reverse()
                items.remove(item)
                items == items.reverse()

    print(items)
    return items



# Best Solution: 
# https://py.checkio.org/mission/when-k-is-enough/publications/tokiojapan55/python-3/first/?ordering=most_voted&filtering=all

def remove_after_kth(items: list, k: int) -> Iterable:
    return [v for i, v in enumerate(items) if items[:i].count(v) < k]



assert list(remove_after_kth([1, 1, 2, 2, 1, 3, 3, 4, 3, 4], 2)) == [1, 1, 2, 2, 3, 3, 4, 4]
assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]

print("The mission is done! Click 'Check Solution' to earn rewards!")