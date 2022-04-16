'https://py.checkio.org/en/mission/lantern-river/'

'''
You are given a map detailing a section of the river as a sequence of strings which forms a matrix. 
Water cells are marked as ".", land cells - "X". In addition, you are given a specified time as a number of minutes from when the lanterns are placed. 
Count how many water cells will are lit at that given time. If a cell is lit by two lanterns at the same time, then count it only once. 
Don't forget count cells where the lanterns are located.
'''

# Best Solution: 
# https://py.checkio.org/mission/lantern-river/publications/vinc/python-3/the-lantern-festival/?ordering=most_voted&filtering=all

from itertools import product

DIRS = {'S': (1, 0), 'N': (-1, 0), 'E': (0, 1), 'W': (0, -1)}

class Lantern:
    def __init__(self, river, cell):
        self.river = river
        self.cell = cell
        self.track = [cell]

    def make_track(self, start, direction):
        """ write track for the lantern using right-hand rule """
        row, col = start
        d = direction
        while row < self.river.finish:
            d_row, d_col = DIRS[d]
            f_cell = (row + d_row, col + d_col)  # forward
            r_cell = (row + d_col, col - d_row)  # right
            l_cell = (row - d_col, col + d_row)  # left
            clean_water = list(filter(self.river.is_clean_water,
                                      (f_cell, r_cell, l_cell)))
            if not clean_water:
                return
            elif len(clean_water) == 1:
                next_cell = clean_water[0]
            else:
                next_cell = r_cell if r_cell in clean_water else f_cell 
            self.track.append(next_cell)
            # find direction for next_cell and repeat loop
            for d in DIRS:
                if (row + DIRS[d][0], col + DIRS[d][1]) == next_cell:
                    row, col = next_cell
                    break

    def move(self, step):
        """ set lantern at track's position """
        if step < len(self.track):
            self.cell = self.track[step]
        else:
            self.cell = self.track[-1]
            
    def lightened_water(self):
        """ return set of lightened water cells by the lantern """
        row, col = self.cell
        return set(filter(self.river.is_water, product((row+1, row, row-1),
                                                       (col+1, col, col-1))))

class River:
    def __init__(self, river_map):
        self.map = river_map
        self.finish = len(river_map)-1
        self.lanterns = [Lantern(self, (0,i)) for i,s in enumerate(river_map[0])
                                              if s == '.']
        self.passed = set()
        for lantern in self.lanterns:
            lantern.make_track(lantern.cell, 'S')
            self.passed.update(lantern.track)

    def flow(self, step):
        """ set all lanterns at their tracks positions """
        for lantern in self.lanterns:
            lantern.move(step)

    def lightened_water(self):
        """ return set of lightened water cells """
        cells = set()
        for lantern in self.lanterns:
            cells.update(lantern.lightened_water())
        return cells

    def is_water(self, cell):
        """ return True if water is at cell """
        row,col = cell
        return (0 <= row < len(self.map) and 0 <= col < len(self.map[0]) and
                self.map[row][col] == '.')
    
    def is_clean_water(self, cell):
        """ return True if cell available for move """
        return self.is_water(cell) and cell not in self.passed

    def print_map(self):
        """ print map with lanterns on it """
        lanterns_on_map = list(self.map)
        for i,lantern in enumerate(self.lanterns):
            row,col = lantern.cell
            lanterns_on_map[row] = lanterns_on_map[row][:col] + str(i) + lanterns_on_map[row][col+1:]
        for row in lanterns_on_map:
            print(row)


def lanterns_flow(river_map, minutes):
    river = River(river_map)
    river.flow(minutes)
    return len(river.lightened_water())


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 0) == 8, "Start"
    assert lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 7) == 18, "7th minute"
    assert lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 9) == 17, "9th minute"