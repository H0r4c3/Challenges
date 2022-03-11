'https://py.checkio.org/en/mission/8-puzzle/'

'''
8 puzzle is a sliding puzzle that consists of a frame of randomly ordered, numbered square tiles with one missing tile. 
The object of the puzzle is to place the tiles in the right order (see picture) by using sliding moves to utilize the empty space.
'''

from typing import List

# Best Solution
# https://py.checkio.org/mission/8-puzzle/publications/sleepyone/python-3/first/share/d763276bd073e88e3d40391b59fcfa87/

import heapq

class PriorityQueue:
    def  __init__(self):
        self.heap = []

    def push(self, item, priority):
        pair = (priority,item)
        heapq.heappush(self.heap,pair)

    def pop(self):
        (priority,item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

def locate_zero(pos):
    for x in range(0, len(pos)):
        for y in range(0, len(pos[x])):
            if pos[x][y] == 0:
                return (x,y)
    return (-1,-1)

moves = [('U', (-1,0)), ('D', (1,0)), ('L', (0,-1)), ('R', (0,1))]

def fix(move, pos, x, y):
    pos = [[y for y in x] for x in pos] # Deepcopy of pos
    d, (dx, dy) = move
    pos[x][y], pos[x+dx][y+dy] = pos[x+dx][y+dy], pos[x][y]
    return (d, pos)

def neighbors(pos):
    x, y = locate_zero(pos)
    m = [m for m in moves if -1 < x+m[1][0] < len(pos) and -1 < y+m[1][1] < len(pos[x])]
    return [fix(move, pos, x, y) for move in m]

def dist(a, b):
    # Hamming distance
    return sum([1 for x in a for y in b if x != y])

def astar(start, goal=[[1,2,3],[4,5,6],[7,8,0]]):
    """
    Notion of a state is represented as the tuple (pos, path).
    seen contains positions.
    """
    seen = set()
    fringe = PriorityQueue()
    fringe.push((start, ''), dist(start, goal))
    while not fringe.isEmpty():
        (pos, path) = fringe.pop()
        key = ''.join([str(el) for row in pos for el in row])
        if key in seen:
            continue
        if pos == goal:
            return path
        seen.add(key)
        for n in neighbors(pos):
            move, newpos = n
            fringe.push((newpos, path + move), dist(newpos, goal) + len(path))
    return ''


def checkio(puzzle):
    ''' 
       Solve the puzzle
      U - up
      D - down
      L - left
      R - right
    '''
    return astar(puzzle)




if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2, 3],
                   [4, 6, 8],
                   [7, 5, 0]]))

    #This part is using only for self-checking and not necessary for auto-testing
    GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def check_solution(func, puzzle):
        size = len(puzzle)
        route = func([row[:] for row in puzzle])
        goal = GOAL
        x = y = None
        for i, row in enumerate(puzzle):
            if 0 in row:
                x, y = i, row.index(0)
                break
        for ch in route:
            swap_x, swap_y = x + MOVES[ch][0], y + MOVES[ch][1]
            if 0 <= swap_x < size and 0 <= swap_y < size:
                puzzle[x][y], puzzle[swap_x][swap_y] = puzzle[swap_x][swap_y], 0
                x, y = swap_x, swap_y
        if puzzle == goal:
            return True
        else:
            print("Puzzle is not solved")
            return False

    assert check_solution(checkio, [[1, 2, 3],
                                    [4, 6, 8],
                                    [7, 5, 0]]), "1st example"
    assert check_solution(checkio, [[7, 3, 5],
                                    [4, 8, 6],
                                    [1, 2, 0]]), "2nd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")