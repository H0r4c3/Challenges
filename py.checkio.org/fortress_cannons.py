'https://py.checkio.org/en/mission/fortress-cannons/'

'''
You have found the enemy . It's the legions of chaos. You are the artillery commander of the fort and it’s up to you to give 
commands so that each cannon shoot at the legions.

The map used in this mission is a hex grid with a maximum size of 12x9, where each hex is numbered from A1 to L9. (A - L indicate a column, and 1 - 9 indicate a row.)

You are given three arguments: the first one is the position of your fort (a string), the second is the specification of each cannon(a list of tuples), and the 
third is the position of enemies (a set of strings).
'''

from itertools import product, chain

DIRECTIONS = ['N', 'NE', 'SE', 'S', 'SW', 'NW']

# Return the coordinates resulting from a move in the specified direction.
def move(coord, direction):
    col, row = coord
    if direction == 0: # N
        return (col, row - 1)
    if direction == 1: # NE
        return (col + 1, (row - 1 if col % 2 else row))
    if direction == 2: # SE
        return (col + 1, (row if col % 2 else row + 1))
    if direction == 3: # S
        return (col, row + 1)
    if direction == 4: # SW
        return (col - 1, (row if col % 2 else row + 1))
    if direction == 5: # NW
        return (col - 1, (row - 1 if col % 2 else row))

# Return a list of all cells covered by the cannon if fired in the specified direction.
def cannon_range(coord, direction, cannon):
    arc, minrange, maxrange = cannon

    result = []

    ldir = (direction - 2) % 6
    rdir = (direction + 2) % 6

    for dist in range(minrange, maxrange + 1):
        point = coord
        for i in range(dist):
            point = move(point, direction)
        result.append(point)

        spread = 0
        if arc == 60:
            spread = dist // 2
        elif arc == 120:
            spread = dist

        point1 = point
        point2 = point
        for i in range(spread):
            point1 = move(point1, ldir)
            result.append(point1)
            point2 = move(point2, rdir)
            result.append(point2)

    return result

# Convert string coord to numeric coord.
def conv_to_coord(coordstr):
    return (ord(coordstr[0]) - ord('A') + 1, int(coordstr[1]))

def fortress_cannons(fort, cannons, enemies):
    fort_coord = conv_to_coord(fort)
    enemy_set = set(conv_to_coord(e) for e in enemies)

    # Point each cannon in each direction and record which enemies get hit.
    cannon_hits = [[enemy_set.intersection(cannon_range(fort_coord, direction, cannon)) for direction in range(6)] for cannon in cannons]

    # Find a set of cannon directions that covers all enemies.
    for dirset in product(range(6), repeat=len(cannons)):
        if enemy_set == set(chain.from_iterable(cannon_hit[direction] for direction, cannon_hit in zip(dirset, cannon_hits))):
            return [DIRECTIONS[direction] for direction in dirset]

    return None


# Best Solution:
# https://py.checkio.org/mission/fortress-cannons/publications/tom-tom/python-3/first/?ordering=most_voted&filtering=all

from itertools import product

def fortress_cannons(fort, cannons, enemies):
    DIRECTION = 'N', 'NE', 'SE', 'S', 'SW', 'NW'
    IN_WEDGE = {0: lambda x, y, z: x == 0 and y > 0,
               60: lambda x, y, z: y >= x >= z,
              120: lambda x, y, z: y >= 0 and z <= 0}
    
    def cube(pos):
        """Cube coordinates"""
        x = ord(pos[0]) - ord('A')
        z = int(pos[1]) - x // 2
        return x, - x - z, z
    
    fort = cube(fort)
    
    #  enemy cube coordinates relative to the fort
    enemies = [tuple(i - j for i, j in zip(cube(enemy), fort)) for enemy in enemies]
    all_enemies = set(range(len(enemies)))

    def can_shoot(cannon, enemy):
        angle, min_distance, max_distance = cannon
        return min_distance <= max(map(abs, enemy)) <= max_distance and IN_WEDGE[angle](*enemy)
    
    #  enemies shot by each cannon in each direction
    reach = [{} for _ in cannons]
    for direction in DIRECTION:
        for n, cannon in enumerate(cannons):
            reach[n][direction] = {i for i, enemy in enumerate(enemies) if can_shoot(cannon, enemy)}
            
        #  rotate enemies around the fort
        enemies = [(-y, -z, -x) for x, y, z in enemies]
    
    for directions in product(DIRECTION, repeat=len(cannons)):
        if set().union(*(reach[n][direction] for n, direction in enumerate(directions))) == all_enemies:
            return list(directions)



if __name__ == '__main__':
    assert fortress_cannons('F5', [(0, 1, 4)], {'F2'}) == ['N'], '0 degree'
    assert fortress_cannons('F5', [(60, 1, 6)], {'K4'}) == ['NE'], '60 degree' 
    assert fortress_cannons('F5', [(120, 1, 4)],{'B3', 'E8'}) == ['SW'], '120 degree'
    assert fortress_cannons('F5', [(0, 2, 6), (120, 1, 3), (60, 1, 4)], {'L2', 'D3', 'C6', 'E9'}) == ['NE', 'NW', 'S'], '3 cannons'
    assert fortress_cannons('F5', [(0, 1, 6), (120, 2, 3)], {'A3', 'E6', 'G7'}) is None, 'None'
    print("Coding complete? Click 'Check' to earn cool rewards!")