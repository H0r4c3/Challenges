'https://py.checkio.org/en/mission/fused-cubes/'

'''
You are given a list of cube details (tuple of 4 integers: X coordinate, Y coordinate, Z coordinate, edge length).

Each coordinate is the minimum value.
All edges parallel to the coordinate axes.
If the cube share the part of another cube or touch with the face of another cube, they are considered as one object.
You should return a list (or iterable) of the volumes of all objects.
'''

from typing import Tuple, List, Iterable


def fused_cubes(cubes: List[Tuple[int]])->Iterable[int]:
    return []



# Best Solution: 
# https://py.checkio.org/mission/fused-cubes/publications/tom-tom/python-3/simple/share/e6b37909b2fe5dd35781b1e0611dfbfb/

from typing import Tuple, List, Iterable
from itertools import product, starmap

def fused_cubes(cubes: List[Tuple[int]])->Iterable[int]:
    """Rerurns list of volumes of the connected objects"""
    cubes = [tuple((e, e + cube[3]) for e in cube[:3]) for cube in cubes]
  
    def fused(a, b):
        s3 = sum((u[0] <= v[1]) and (v[0] <= u[1]) for u, v in zip(a, b))
        s2 = sum((u[0] < v[1]) and (v[0] < u[1]) for u, v in zip(a, b))
        return s3 == 3 and s2 >= 2
    
    groups = set()
    for cube in cubes:
        connected = {g for g in groups if any(fused(c, cube) for c in g)}
        new_group = frozenset((cube,)).union(*connected)
        groups = groups.difference(connected) | {new_group}
    
    # this works well only if the cubes are not very large
    return [len({xyz for cube in group for xyz in product(*starmap(range, cube))})
            for group in groups]



# Best Solution: 
# https://py.checkio.org/mission/fused-cubes/publications/CDG.Axel/python-3/8-lines-proc/?ordering=most_voted&filtering=all

def fused_cubes(cubes, prod=__import__('itertools').product):
    shifts, ci = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], 0
    cubes = [set(prod(range(x, x+l), range(y, y+l), range(z, z+l))) for x, y, z, l in cubes]
    while ci < len(cubes):
        for i in range(ci):
            if cubes[i] & {(x+dx, y+dy, z+dz) for x, y, z in cubes[ci] for dx, dy, dz in shifts}:
                cubes[ci: ci+1], _, ci = [], cubes[i].update(cubes[ci]), 0
        ci += 1
    return [len(cube) for cube in cubes]



if __name__ == '__main__':
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52], 'fused'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)])) == [54], 'touch with faces'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27], 'touch with edges'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 3, 3, 3)])) == [27, 27], 'touch with vertices'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 4, 3, 3)])) == [27, 27], 'separated'
    assert sorted(fused_cubes([(0, 0, 0, 3), (-2, -2, -2, 3)])) == [53], 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")