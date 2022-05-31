'https://py.checkio.org/en/mission/ore-in-the-desert/'

'''
The desert has a size of 10x10 cells and can be represented as a 2D array. 
The ship has four probes which can be used to help us find the ore. 
At each step you will need to return the coordinates of a cell (as [row, column]) for the probe to travel to. 
If the cell contains ore, then you can finish; else the probe will give a distance to the 
location of the ore cell (it will be the Euclidean distance between cells' centers).
'''

def checkio(previous):
    return [0, 0]



# Best Solution: 
# https://py.checkio.org/mission/ore-in-the-desert/publications/bryukh/python-3/second/?ordering=most_voted&filtering=all

from math import hypot

cells = [[i, j] for i in range(10) for j in range(10)]

def checkio(data):
    global cells
    for x, y, d in data[-1:]:
        cells = [[i, j] for i, j in cells if round(hypot(x - i, y - j), 0) == d]
    return cells[0]



# Best Solution: 
# https://py.checkio.org/mission/ore-in-the-desert/publications/Somebody12345678910/python-3/first/share/cfd025f75ab8af45fba32a31dff34a9c/

import itertools
import random

candidates = None

def checkio(previous):
    global candidates
    times = len(previous)
    if times == 0:
        candidates = list(itertools.product(range(10), repeat=2))
        candidates.remove((0, 0))
        return [0, 0]

    p = previous[-1]
    remove = []
    for d in candidates:
        if round(((d[0] - p[0]) ** 2 + (d[1] - p[1]) ** 2) ** .5) != p[2]:
            remove.append(d)
    for r in remove:
        candidates.remove(r)
    c = random.choice(candidates)
    return c





if __name__ == '__main__':
    #This part is using only for self-testing.
    def check_solution(func, ore):
        recent_data = []
        for step in range(4):
            row, col = func([d[:] for d in recent_data])  # copy the list
            if row < 0 or row > 9 or col < 0 or col > 9:
                print("Where is our probe?")
                return False
            if (row, col) == ore:
                return True
            dist = round(((row - ore[0]) ** 2 + (col - ore[1]) ** 2) ** 0.5)
            recent_data.append([row, col, dist])
        print("It was the last probe.")
        return False

    assert check_solution(checkio, (1, 1)), "Example"
    assert check_solution(checkio, (9, 9)), "Bottom right"
    assert check_solution(checkio, (6, 6)), "Center"
    print("Done!!!")