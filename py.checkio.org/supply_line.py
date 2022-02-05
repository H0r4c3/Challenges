'https://py.checkio.org/en/mission/supply-line/'

'''
You should find the shortest supply line with Python.

The map used in this mission is a hex grid with a maximum size of 12x9 where each hex is 
numbered from A1 to L9. (A - L indicate a column, and 1 - 9 indicate a row.)

You are given three arguments: the first is the position of your uint (a string), the second is the supply depots (the set of strings), 
and the third is the enemy units (the set of strings). You should return the minimum number of steps from your unit to the supply depot. If you can’t set a supply line at all, return None.

The effect of the enemy hex and its adjacent hexes:

You can’t lay the supply lines on these hexes.
If your unit is adjacent to the enemy’s, there is no problem with the supply line.
The supply depot on these hexes can’t be used .
'''



'''
https://stackoverflow.com/questions/15919783/distance-between-2-hexagons-on-hexagon-grid
The correct explicit formula for the distance:
d((x1,y1),(x2,y2)) = max(abs(x1 - x2), abs((y1 + floor(x1/2)) - (y2 + floor(x2/2))))
d((x1,y1),(x2,y2)) = max(abs(x1-x2), abs(y1-y2))
'''


# Best Solution:
# https://py.checkio.org/mission/supply-line/publications/flpo/python-3/reduce-or_-starmap/share/6043bc39d6beb17b16b3becf8cc8272c/

from functools import reduce
from operator import or_
from itertools import starmap

GRID = {(col, row) for col in range(ord('A'), ord('L') + 1) for row in range(1, 10)}
print(GRID)

def neighbors(c, r):
    if c % 2:
        return {(c, r-1), (c+1, r-1), (c+1, r), (c, r+1), (c-1, r), (c-1, r-1)} 
    else:
        return {(c, r-1), (c+1, r), (c+1, r+1), (c, r+1), (c-1, r+1), (c-1, r)}

def expand(positions):
    return reduce(or_, starmap(neighbors, positions), positions) & GRID

def coords(c, r):
    return ord(c), int(r)

def coords_set(positions):
    return set(starmap(coords, positions))

        

def supply_line(pos, supply, enemies):
    visited = expand(coords_set(enemies))
    supply = coords_set(supply) - visited

    steps, to_visit = 0, {coords(*pos)}
    while to_visit:
        steps += 1
        to_visit = expand(to_visit) - visited
        visited |= to_visit
        if visited & supply:
            print(steps)
            return steps
        


if __name__ == '__main__':
    assert supply_line("B4", {"F4"}, {"D4"}) == 6, 'simple'
    assert supply_line("A3", {"A9", "F5", "G8"}, {"B3", "G6"}) == 11, 'multiple'
    assert supply_line("C2", {"B9", "F6"}, {"B7", "E8", "E5", "H6"}) is None, 'None'
    assert supply_line("E5", {"C2", "B7", "F8"}, set()) == 4, 'no enemies'
    assert supply_line("A5", {"A2", "B9"}, {"B3", "B7", "E3", "E7"}) == 13, '2 depots'
    print('"Run" is good. How is "Check"?')