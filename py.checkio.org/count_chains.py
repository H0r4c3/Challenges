'https://py.checkio.org/en/mission/count-chains/'

'''
In this mission you must count chains.

You are given a list of details of the circle (tuple of X-coordinate, Y-coordinate, radius).
You have to return the number of groups of circles where their circumferences intersect.

NOTE:
Only one circle counts as one group.

Input:
A list of details of the circle.
Details of the circle is a tuple of three integers(X-coordinate, Y-coordinate, radius).
Output: An integer.
'''

#https://py.checkio.org/mission/count-chains/publications/tom-tom/python-3/first/share/c01fc6f6d132c3bff495c7be96c61069/
import math
from typing import List, Tuple

def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    def inter(a, b):
        return abs(a[2] - b[2]) < math.dist(a[:2], b[:2]) < a[2] + b[2]
    
    groups = set()
    for circle in circles:
        connected = {g for g in groups if any(inter(c, circle) for c in g)}
        new_group = frozenset((circle,)).union(*connected)
        groups = groups.difference(connected) | {new_group}
    return len(groups)


# https://py.checkio.org/mission/count-chains/publications/flpo/python-3/circle-intersection/?ordering=most_voted&filtering=all
from sympy.geometry import Circle
from sympy.geometry.util import intersection

def count_chains(coords):
    circles = [Circle((x, y), r) for x, y, r in sorted(coords)]
    def close(circle):
        for other in circles:
            if len(intersection(other, circle)) > 1:
                circles.remove(other)
                close(other)
    chains = 0
    while circles:
        chains += 1
        close(circles.pop())
    return chains




if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")