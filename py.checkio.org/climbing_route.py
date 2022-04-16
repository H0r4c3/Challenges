'https://py.checkio.org/mission/climbing-route/publications/tom-tom/python-3/first/share/0af7783a906546e8122c219f849b0b50/'

'''
You have an elevation map and you want to know the shortest climbing route.

The map is given as a list of strings.

0 : plain ( elevation is 0)
1-9 : hill (number is elevation)
"mountain" is adjacent (only 4 directions) hill group.

It consists of two or more hills.
Isolated hill is not mountain.
The highest elevation is the mountaintop that is always only one.
'''

# Best Solution: 
# https://py.checkio.org/mission/climbing-route/publications/tom-tom/python-3/first/share/0af7783a906546e8122c219f849b0b50/

from functools import partial
from collections import deque
from itertools import permutations

def climbing_route(elevation_map):
    range_i, range_j = range(len(elevation_map)), range(len(elevation_map[0]))
    start, goal = (0, 0), (range_i[-1], range_j[-1])
    hills = {(i, j) for i, row in enumerate(elevation_map)
                        for j, c in enumerate(row) if c != '0'}
    def height(pos):
        return int(elevation_map[pos[0]][pos[1]])

    def neighbours(pos):
        x, y = pos
        for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if i in range_i and j in range_j:
                yield (i, j)
                
    def mountains():
        def mountain(hill):
            hills.discard(hill)
            return {hill}.union(*(map(mountain, filter(hills.__contains__, neighbours(hill)))))
        
        while hills:
            yield mountain(hills.pop())
            
    # find top of every mountain
    tops = set(map(partial(max, key=height), filter(lambda m: len(m) > 1, mountains())))

    # find distances between mountaintops, start, and goal
    distance = {}
    for seed in {start} | tops:
        dist = {}
        active = deque()
        dist[seed] = 0
        active.append(seed)
        while active:
            pos = active.popleft()
            pos_dist, pos_height = dist[pos], height(pos)
            for new_pos in neighbours(pos):
                if new_pos not in dist and abs(pos_height - height(new_pos)) <= 1:
                    dist[new_pos] = pos_dist + 1
                    active.append(new_pos)
        distance.update({(seed, top): dist[top] for top in tops | {goal}})

    # find minimum path length
    return min(sum(distance[pair] for pair in zip((start,) + p, p + (goal,)))
               for p in permutations(tops))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert climbing_route([
        '000',
        '210',
        '000']) == 6, 'basic'
    assert climbing_route([
        '00000',
        '05670',
        '04980',
        '03210',
        '00000']) == 26, 'spiral'
    assert climbing_route([
        '000000001',
        '222322222',
        '100000000']) == 26, 'bridge'
    assert climbing_route([
        '000000002110',
        '011100002310',
        '012100002220',
        '011100000000']) == 26, 'two top'
    assert climbing_route([
        '000000120000',
        '001002432100',
        '012111211000',
        '001000000000']) == 16, 'one top'
    assert climbing_route([
        '00000000111111100',
        '00000000122222100',
        '00000000123332100',
        '00000000123432100',
        '00000000123332100',
        '00000000122222100',
        '00000000111111100',
        '00011111000000000',
        '00012221000000000',
        '00012321000000000',
        '00012221000000012',
        '00011111000000000',
        '11100000000000000',
        '12100000000000000',
        '11100000000000000']) == 52, 'pyramids'
    
    print('Done!!!')