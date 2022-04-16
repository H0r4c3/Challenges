'https://py.checkio.org/en/mission/landing-site/'

'''
In this mission the size of the hexagonal grid is 12x9 ('A1' to 'L9').

It’s characteristics:
it’s flat-topped;
the alphabet letters represent columns and numbers represent rows;
the even columns are being pushed down.
You are given a set of obstacle hexes on the Moon as an input value. You have to return a set of all the candidate landing sites.

The conditions for the landing site hex:
the hex isn't an obstacle hex;
there’re no obstacle hexes in equidistant ( 1 or more ) hexes;
the above radius is the longest.
NOTE:
The outside of the hexagonal grid is always considered as an obstacle hex.
If there aren’t any landing sites, return an empty set.
'''

from typing import Set

def landing_site(obstacles: Set[str]) -> Set[str]:
    return set()



# Best Solution: 
# https://py.checkio.org/mission/landing-site/publications/veky/python-3/deqtuenary/share/4b7b3ff90219846085ed0888b171a228/

import typing, collections, itertools, string

def neighbors(hex):
    j, i = hex
    for t in -1, 1:
        yield j, i + t
        for s in 0, (-1)**j: yield j + t, i + s

to_coords = lambda hex: (int(hex[0], 36) - 9, int(hex[1]))
from_coords = lambda hex: string.ascii_uppercase[hex[0] - 1] + str(hex[1])
visible = {*itertools.product(range(1, 13), range(1, 10))}
outer = {*itertools.product(range(-1, 15), range(-1, 12))} - visible

def landing_site(obstacles: {str}) -> {str}:
    obstacles = {*map(to_coords, obstacles)} | outer
    free = visible - obstacles    
    q = collections.deque((pos, 0) for pos in obstacles)
    distance = {}
    while q:
        old, n = q.popleft()
        distance[old] = n
        for new in neighbors(old):
            if new in free: q.append((new, n + 1))
            free.discard(new)
    md = max(distance.values())
    return {from_coords(pos) for pos, d in distance.items() if d == md > 1}



if __name__ == '__main__':
    assert landing_site({'E5', 'E7', 'F4', 'F6', 'G4', 'G6', 'H3', 'H5'}) == {'C3', 'J7'}, 'crevasse'
    assert landing_site({'A4', 'C2', 'C6', 'C9', 'D4', 'D7', 'F1', 'F5',
                         'F8', 'G4', 'H7', 'I2', 'I5', 'I9', 'K3', 'K8', 'L5'}) == {'B7', 'E3', 'J6'}, 'stones'
    assert landing_site({'D3', 'D4', 'D5', 'D6', 'E3', 'E7', 'F2', 'F7', 'G2',
                         'G8', 'H2', 'H7', 'I3', 'I7', 'J3', 'J4', 'J5', 'J6'}) == {'G5'}, 'crater'
    assert landing_site(set()) == {'E5', 'F5', 'G5', 'H5'}, 'plane'
    assert landing_site({chr(c+65)+str(r+1) for c in range(12) for r in range(9)}) == set(), 'wasteland'

    print('The local tests are done. Click on "Check" for more real tests.')
