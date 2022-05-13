'https://py.checkio.org/en/mission/strange-curcuit/'

'''
The map of the circuit consists of a series of square cells. 
The first element in the center is marked as 1, and continuing in a clockwise spiral, each other elements is marked in ascending order. 
On the map, you can move (connect cells) vertically and horizontally. 
You can help Nikola find the manhattan distance between any two elements on the map. For example, the distance between cells 1 and 9 is 
two moves and the distance between 24 and 9 is one move.
'''

from itertools import product
from pandas.core.common import flatten

# My Solution = not finished, yet
def find_distance(first, second):
    SPIRAL_3X3 = {1:[1, 1], 2:[1, 0], 3:[2, 0], 4:[2, 1], 5:[2, 2], 6:[1, 2], 7:[0, 2], 8:[0, 1], 9:[0, 0]}
    
    SPIRAL_5X5 = {1:[2, 2],  2:[2, 1],  3:[3, 1],  4:[3, 2],  5:[3, 3],  6:[2, 3],  7:[1, 3],  8:[1, 2], 9:[1, 1],
                 10:[0, 1], 11:[0, 2], 12:[0, 3], 13:[0, 4], 14:[4, 1], 15:[4, 2], 16:[4, 3], 17:[4, 4], 
                 18:[3, 4], 19:[2, 4], 20:[1, 4], 21:[0, 4], 22:[0, 3], 23:[0, 2], 24:[0, 1], 25:[0, 0]}
    
    MATRIX_3X3 = [[9, 2, 3],
                  [8, 1, 4],
                  [7, 6, 5]]
    
    MATRIX_5X5 = [[25, 10, 11, 12, 13],
                  [24, 9,  2,  3,  14],
                  [23, 8,  1,  4,  15],
                  [22, 7,  6,  5,  16],
                  [21, 20, 19, 18, 17]]
    
    MATRIX_5X5 = list(flatten(MATRIX_5X5))
    
    MATRIX_7X7 = [[49, 26, 27, 28, 29, 30, 31],
                  [48, 25, 10, 11, 12, 13, 32],
                  [47, 24, 9,  2,  3,  14, 33],
                  [46, 23, 8,  1,  4,  15, 34],
                  [45, 22, 7,  6,  5,  16, 35],
                  [44, 21, 20, 19, 18, 17, 36],
                  [43, 42, 41, 40, 39, 38, 37]]
    
    MATRIX_7X7 = list(flatten(MATRIX_7X7))
    
    MATRIX_9X9 = [[81, 50, 51, 52, 53, 54, 55, 56, 57],
                  [80, 49, 26, 27, 28, 29, 30, 31, 58],
                  [79, 48, 25, 10, 11, 12, 13, 32, 59],
                  [78, 47, 24, 9,  2,  3,  14, 33, 60],
                  [77, 46, 23, 8,  1,  4,  15, 34, 61],
                  [76, 45, 22, 7,  6,  5,  16, 35, 62],
                  [75, 44, 21, 20, 19, 18, 17, 36, 63],
                  [74, 43, 42, 41, 40, 39, 38, 37, 64],
                  [73, 72, 71, 70, 69, 68, 67, 66, 65]]
    
    MATRIX_9X9 = list(flatten(MATRIX_9X9))
    
    MATRIX_11X11 = [[121, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91],
                    [120, 81, 50, 51, 52, 53, 54, 55, 56, 57, 92],
                    [119, 80, 49, 26, 27, 28, 29, 30, 31, 58, 93],
                    [118, 79, 48, 25, 10, 11, 12, 13, 32, 59, 94],
                    [117, 78, 47, 24, 9,  2,  3,  14, 33, 60, 95],
                    [116, 77, 46, 23, 8,  1,  4,  15, 34, 61, 96],
                    [115, 76, 45, 22, 7,  6,  5,  16, 35, 62, 97],
                    [114, 75, 44, 21, 20, 19, 18, 17, 36, 63, 98],
                    [113, 74, 43, 42, 41, 40, 39, 38, 37, 64, 99],
                    [112, 73, 72, 71, 70, 69, 68, 67, 66, 65, 100],
                    [111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101]]
    
    MATRIX_11X11 = list(flatten(MATRIX_11X11))
    
    
    coords_3 = list(product([0, 1, 2], [0, 1, 2]))
    print(coords_3) # [(0, 0), (0, 1), (0, 2), 
                      #(1, 0), (1, 1), (1, 2), 
                      #(2, 0), (2, 1), (2, 2)]
                      
    coords_5 = list(product([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]))
    print(coords_5) # [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), 
                     # (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), 
                     # (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), 
                     # (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), 
                     # (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
                     
    coords_7 = list(product([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6]))
    
    coords_9 = list(product([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]))
    
    coords_11 = list(product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
                     
                     
    SPIRAL_5 = dict(zip(MATRIX_5X5, coords_5))
    print(SPIRAL_5)
    
    SPIRAL_7 = dict(zip(MATRIX_7X7, coords_7))
    print(SPIRAL_7)
    
    SPIRAL_9 = dict(zip(MATRIX_9X9, coords_9))
    print(SPIRAL_9)
    
    SPIRAL_11 = dict(zip(MATRIX_11X11, coords_11))
    print(SPIRAL_11)
                     
    # At first, we determine ring which include n
    # ring 0 : 1
    # ring 1 : 2, 3, ..., 9 = range(2, 10)
    # ring 2 : 10, 11, ..., 25 = range(10, 26)
    # ...
    # ring r : (2*r-1)**2 + 1, ... , (2*r+1)**2
    
    print(first, second)
    n = max(first, second)
    r = int(((n-1)**0.5 + 1) / 2)
    print(r)
    
    (x1,y1) = SPIRAL_11[first]
    (x2,y2) = SPIRAL_11[second]
    
    return abs(x1-x2) + abs(y1-y2)
    
    




# Best Solution: 
# https://py.checkio.org/mission/strange-curcuit/publications/David_Jones/python-3/first/share/2d5270983c4c1df35897635394f2482c/

def coords(n):
    if n == 1:
        return (0,0)
    r = int(((n-1)**0.5 + 1) / 2)
    side, n = divmod(n - (2*r - 1)**2 - 1, 2*r)
    print(side, n)
    n += 1-r
    if side == 0:
        return (r, n)
    if side == 1:
        return (-n, r)
    if side == 2:
        return (-r, -n)
    return (n, -r)

def find_distance_(first, second):
    (x1,y1) = coords(first)
    (x2,y2) = coords(second)
    return abs(x1-x2) + abs(y1-y2)


# Another Best Solution:
# https://py.checkio.org/mission/strange-curcuit/publications/Sim0000/python-3/direct-calculation/?ordering=most_voted&filtering=all

from math import sqrt

# calculate the coordinate of n
def coord(n):
    if n == 1: return (0, 0)
    r = int(sqrt(n - 1) - 1) // 2 + 1
    g, d = divmod(n - (2*r-1)**2 - 1, 2*r)
    return [(-r+d+1, r), (r, r-d-1), (r-d-1, -r), (-r, -r+d+1)][g]

def find_distance(first, second):
    x1, y1 = coord(first)
    x2, y2 = coord(second)
    return abs(x2 - x1) + abs(y2 - y1)

    # At first, we determine ring which include n
    #   ring 0 : 1
    #   ring 1 : 2,3,...,9
    #   ring 2 : 10,11,...,25
    #   ring r : (2*r-1)**2+1,...,(2*r+1)**2
    # Using following formula, we can calculate r from n.
    #   r = int((sqrt(n - 1) - 1) / 2) + 1
    # Ring r have 8*r elements and start position is (-r+1, r).
    # And another interesting position is follows.
    #   (-r,  r) : left upper corner,  n = (2*r-1)**2 + 8*r = (2*r+1)**2
    #   ( r,  r) : right upper corner, n = (2*r-1)**2 + 2*r
    #   ( r, -r) : right lower corner, n = (2*r-1)**2 + 4*r
    #   (-r, -r) : left lower corner,  n = (2*r-1)**2 + 6*r
    #
    # Second, I divide ring into 4 groups corresponding to the direction.
    # Each group size is 2*r. The group 0 is the first 2*r elements of the ring
    # and its direction is right, and so on.
    #   group 0 (dir = R) : n is from (2*r-1)**2    +1 to (2*r-1)**2+2*r
    #   group 1 (dir = D) : n is from (2*r-1)**2+2*r+1 to (2*r-1)**2+4*r
    #   group 2 (dir = L) : n is from (2*r-1)**2+4*r+1 to (2*r-1)**2+6*r
    #   group 3 (dir = U) : n is from (2*r-1)**2+6*r+1 to (2*r-1)**2+8*r
    # Using following formula, we can calculate group number g from n, r.
    #   g = int((n - (2*r-1)**2 - 1) / (2*r)
    #
    # Finally, using above information, we will calulate the coordinate of n.
    # When n belongs to group 0 of ring r, then the coordinate of n is
    # (-r+1 + d, r), where d means n is the d-th elements of the group.
    # As well, we can calculate for another groups.
    #   group 0 : (-r+1+d, r)
    #   group 1 : (r, r-1+d)
    #   group 2 : (r-1-d, r)
    #   group 3 : (-r, -r+d+1)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"
    assert find_distance(99, 1) == 8
    print('Done!!!')