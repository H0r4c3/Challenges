'https://py.checkio.org/en/mission/shortest-knight-path/'

'''
You are given the start and end squares as chess coordinates separated by a hyphen. 
You should find the length of the shortest path for the knight from one point to another on the chessboard.
'''

    
import itertools as it
from string import ascii_lowercase as alpha


# https://ats-min.com/?p=394
def checkio(cells):
    """str -> int
    Number of moves in the shortest path of knight
    """
    restrict = lambda c: 0 < c[0] < 9 and 0 < c[1] < 9
    calc_reachable = lambda a, b: list(
        filter(restrict, it.chain(
            ((a + x, b + y) for x in (-2, 2) for y in (-1, 1)),
            ((a + x, b + y) for y in (-2, 2) for x in (-1, 1)),
        )))
    to_num = lambda x: alpha.index(x) + 1 if x.isalpha() else int(x)
    start, goal = (tuple(map(to_num, x)) for x in cells.split('-'))
    reachable = (start,)
    for count in it.count(1):
        reachable = set(it.chain.from_iterable(
            calc_reachable(*c) for c in reachable
        ))
        if goal in reachable:
            return count

    return 0


# Best Solution: 
# https://py.checkio.org/mission/shortest-knight-path/publications/tom-tom/python-3/first/?ordering=most_voted&filtering=all

def checkio(cells: str) -> int:
    """Number of moves in the shortest path of knight"""
    
    def moves(cell):
        x, y = map(ord, cell)
        for move in ((x + 1, y + 2), (x + 2, y + 1), (x - 1, y + 2), (x - 2, y + 1),
                     (x + 1, y - 2), (x + 2, y - 1), (x - 1, y - 2), (x - 2, y - 1)):
            ca, cb = map(chr, move)
            if ca in 'abcdefgh' and cb in '12345678':
                yield ca + cb
                
    start, end = cells.split('-')
    visited, current = set(), {start}
    for step in range(1, 100):
        visited |= current
        new = {new_cell for cell in current for new_cell in moves(cell)} - visited
        if end in new:
            return step
        current = new

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"
    print('Done!')