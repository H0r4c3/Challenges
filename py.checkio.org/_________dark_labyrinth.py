'https://py.checkio.org/en/mission/dark-labyrinth/'

'''

'''

# Best Solution:
# https://py.checkio.org/mission/dark-labyrinth/publications/Sim0000/python-3/first/?ordering=most_voted&filtering=all

from collections import Counter

DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
m = Counter()
x = 0
y = 0

def find_path(visible):
    global x, y # player position for m

    # increment visit count
    m[(x, y)] += 1
    
    # find player position in visible
    xp, yp = next((x, y) for y, row in enumerate(visible) for x, c in enumerate(row) if c == 'P')

    # find direction of minimum visit count
    v = []
    for d in 'NESW':
        dy, dx = DIR[d]
        if visible[yp + dy][xp + dx] in '.E':
            x0, y0 = x + dx, y + dy
            if not v or m[(x0, y0)] < v[0]:
                v = [m[(x0, y0)], d, x0, y0]

    x, y = v[2], v[3] # next position
    return v[1] # direction

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    PLAYER = "P"
    WALL = "X"
    UNKNOWN = "?"
    EXIT = "E"
    EMPTY = "."
    MAX_STEP = 250

    def clear_zone(zone):
        return [row for row in zone if not all(el == UNKNOWN for el in row)]

    def get_visible(maze, player):
        grid = [["?" for _ in range(len(row))] for row in maze]
        grid[player[0]][player[1]] = PLAYER
        for direction, diff in DIR.items():
            r, c = player
            while maze[r][c] != WALL:
                r, c = r + diff[0], c + diff[1]
                grid[r][c] = maze[r][c]
                if direction in "NS":
                    grid[r + DIR["W"][0]][c + DIR["W"][1]] = maze[r + DIR["W"][0]][c + DIR["W"][1]]
                    grid[r + DIR["E"][0]][c + DIR["E"][1]] = maze[r + DIR["E"][0]][c + DIR["E"][1]]
                else:
                    grid[r + DIR["S"][0]][c + DIR["S"][1]] = maze[r + DIR["S"][0]][c + DIR["S"][1]]
                    grid[r + DIR["N"][0]][c + DIR["N"][1]] = maze[r + DIR["N"][0]][c + DIR["N"][1]]
        grid = clear_zone(list(zip(*clear_zone(grid))))
        return tuple("".join(trow) for trow in zip(*grid))

    def initial(maze, player):
        return maze, get_visible(maze, player)

    def checker(func, player, maze):
        step = 0
        while True:
            result = func(get_visible(maze, player))
            if not isinstance(result, str) or any(ch not in DIR.keys() for ch in result):
                print("The function should return a string with directions.")
                return False

            for act in result:
                if step >= MAX_STEP:
                    print("You are tired and your flashlight is off. Bye bye.")
                    return False
                r, c = player[0] + DIR[act][0], player[1] + DIR[act][1]
                if maze[r][c] == WALL:
                    print("BAM! You in the wall at {}, {}.".format(r, c))
                    return False
                elif maze[r][c] == EXIT:
                    print("GRATZ!")
                    return True
                else:
                    player = r, c
                    step += 1

    assert checker(find_path, (1, 1), [
        "XXXXXXX",
        "X.....X",
        "X.X.X.X",
        "X.....X",
        "X.X.X.X",
        "X.X.E.X",
        "XXXXXXX",
    ]), "Simple"
    assert checker(find_path, (1, 4), [
        "XXXXXXXXXX",
        "X....X...X",
        "X.XXXX.X.X",
        "X....X.X.X",
        "X.XXXX.X.X",
        "X.X....X.X",
        "X.XXEX.X.X",
        "X.XXXXXX.X",
        "X........X",
        "XXXXXXXXXX",
    ]), "First"
    assert checker(find_path, (10, 10), [
        "XXXXXXXXXXXX",
        "XX...X.....X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "XE.X.....X.X",
        "XXXXXXXXXXXX",
    ]), "Up down"
