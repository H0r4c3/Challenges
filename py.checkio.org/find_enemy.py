'https://py.checkio.org/en/mission/find-enemy/'

'''
Find the distance and directions to an enemy in a HEX-grid.

Input: Three arguments: your current coordinates, your current absolute directions, and enemy's coordinates.

Output: A list with relative directions and distance to the enemy.
'''

from math import sin, cos, acos, hypot, degrees, pi
from operator import mul

def find_enemy(you, dir, enemy):
    x, y = zip(you, enemy)
    x = [ord(L)-65 for L in x]
    y = [int(n) + x[i] % 2 / 2 for i, n in enumerate(y)]
    u = [(x[1] - x[0]) * sin(pi/3), y[1] - y[0]]
    a = {'N': pi, 'NE': pi*2/3, 'SE': pi/3, 'S': 0, 'SW': pi*5/3,
         'NW': pi*4/3}.get(dir)
    v = [sin(a), cos(a)]
    angle = degrees(acos(sum(map(mul, u, v)) / hypot(*u)))
    if angle < 59.9:
        result = ['F']
    elif angle < 120.1:
        left = u[0] * v[1] - u[1] * v[0] > 0
        result = [['R', 'L'][left]]
    else:
        result = ['B']
    dist = abs(u[0] / sin(pi/3))
    dist += max(0, abs(u[1]) - dist * .5)
    result.append(round(dist))
    return result



# https://py.checkio.org/mission/find-enemy/publications/tom-tom/python-3/hex-coords/?ordering=most_voted&filtering=all
def find_enemy_2(you, abs_dir, enemy):

    def hex_coords(pos):
        j = ord(pos[0]) - ord('A')
        i = int(pos[1]) - j // 2 - 1
        return i, j

    i1, j1 = hex_coords(you)
    i2, j2 = hex_coords(enemy)
    x, y = i2 - i1, j2 - j1
    distance = max(abs(x), abs(y), abs(x + y))
    x, y = {'N': (-x, -y), 'NE': (y, -x - y), 'SE': (x + y, -x),
            'S': (x, y), 'SW': (-y, x + y), 'NW': (-x - y, x)}[abs_dir]
    if y > 0 and -y <= x <= 0:
        rel_dir = 'L'
    elif y < 0 and 0 <= x <= - y:
        rel_dir = 'R'
    elif x > 0:
        rel_dir = 'F'
    else:
        rel_dir = 'B'
    return [rel_dir, distance]


if __name__ == '__main__':
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")