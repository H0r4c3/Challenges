'https://py.checkio.org/en/mission/express-delivery/'

'''
The map for delivery is presented as an array of strings, where:

"W" is a water (closed cell)
"B" is a box
"E" is a goal point.
"S" is a start point.
"." is an empty cell.
Stephan moves between neighbouring cells in two minutes if he carries a load. Without any carry-on luggage, he only needs one minute. 
Loading and unloading of cargo in (and out of) the box takes one minute. You should find the fastest way for the cargo delivery (minimum time).

The route is a string, where each letter is an action.

"U" -- Up (north)
"D" -- Down (south)
"L" -- Left (west)
"R" -- Right (east)
"B" -- Load or unload in (out) a box.
'''

from typing import List

def checkio(field_map: List[str]) -> str:
    return "RRRDDD"



# Best Solution:
# https://py.checkio.org/mission/express-delivery/publications/DiZ/python-3/branch-if-box/?ordering=most_voted&filtering=all

from heapq import heappush, heappop

def checkio(field):
    dirs = {'D':(1,0), 'U':(-1,0), 'R':(0,1), 'L':(0,-1)}
    start = next((i, j) for i, l in enumerate(field) for j, c in enumerate(l) if c == 'S')
    seen, bag = set(), [(0, True, start, '')]
    while bag:
        score, cargo, (x, y), path = heappop(bag)
        if cargo and field[x][y] == 'E': return path
        seen.add((cargo, (x, y)))
        if field[x][y] == 'B':
            heappush(bag, [score + 1, not cargo, (x, y), path + 'B'])
        for direction, (u, v) in dirs.items():
            xn, yn = u + x, v + y
            if (cargo, (xn, yn)) in seen: continue
            if 0 <= xn < len(field) and 0 <= yn < len(field[0]) and field[xn][yn] != 'W':
                heappush(bag, [score + 1 + cargo, cargo, (xn, yn), path + direction])
                
                
                



# Best Solution:
# https://py.checkio.org/mission/express-delivery/publications/blabaster/python-3/first/share/0fc1f7ff974df213046ca8d7198eb523/

from heapq import heappop, heappush


def checkio_(field_map):
    height, width = len(field_map), len(field_map[0])

    def neighbours(col, row):
        if row:
            yield col, row - 1, 'U'
        if row < height - 1:
            yield col, row + 1, 'D'
        if col:
            yield col - 1, row, 'L'
        if col < width - 1:
            yield col + 1, row, 'R'

    for y, s in enumerate(field_map):
        x = s.find('S')
        if x >= 0:
            queue = [(0, x, y, True, None, None)]  #time, x, y, cargo, letter, prev
    visited = [set(), set()]
    while True:
        time, x, y, cargo, letter, prev = cur = heappop(queue)
        if cargo and field_map[y][x] == 'E':
            res = []
            while prev:
                res.append(letter)
                time, x, y, cargo, letter, prev = prev
            return ''.join(reversed(res))
        visited[cargo].add((x, y))
        if field_map[y][x] == 'B' and (x, y) not in visited[not cargo]:
            heappush(queue, (time + 1, x, y, not cargo, 'B', cur))
        for x1, y1, letter in neighbours(x, y):
            if (x1, y1) not in visited[cargo] and field_map[y1][x1] in '.BES':
                heappush(queue, (time + cargo + 1, x1, y1, cargo, letter, cur))



if __name__ == '__main__':
    print("Example:")
    print(checkio(["S...", "....", "B.WB", "..WE"]))

    #This part is using only for self-checking and not necessary for auto-testing
    ACTIONS = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
        "B": (0, 0)
    }

    def check_solution(func, max_time, field):
        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False

    assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")