'https://py.checkio.org/en/mission/shoot-range/'

'''
Input: Four arguments. Two wall ends, a firing point and a later point as tuples of two numbers.

Output: The results as an integer from -1 to 100.
'''

# My Solution (incomplete!!!!!!!)

from math import dist, acos, degrees, sin, pi, sqrt
from re import L

def collinear(x1, y1, x2, y2, x3, y3): 
    """ Python program to check if three points are collinear or not using area of triangle."""
    
    # Calculation the area of triangle. We have skipped multiplication with 0.5 to avoid floating point computations    
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 
  
    return a


# returns square of distance b/w two points
def lengthSquare(X, Y):
    xDiff = X[0] - Y[0]
    yDiff = X[1] - Y[1]
    return xDiff * xDiff + yDiff * yDiff
     
def angle(A, B, C):
    '''
    Calculates the angles
    '''
     
    # Square of lengths be a2, b2, c2
    a2 = lengthSquare(B, C)
    b2 = lengthSquare(A, C)
    c2 = lengthSquare(A, B)
 
    # length of sides are a, b, c
    a = sqrt(a2)
    b = sqrt(b2)
    c = sqrt(c2)
 
    # From Cosine law
    #alpha = acos((b2 + c2 - a2) / (2 * b * c))
    beta = acos((a2 + c2 - b2) / (2 * a * c))
    #gamma = acos((a2 + b2 - c2) / (2 * a * b))
 
    
    #return degrees(beta), degrees(gamma), degrees(alpha)
    return degrees(beta)
    


def shot(wall1, wall2, shot_point, later_point):
    # length of the wall
    w = dist(wall1, wall2)
    print(f'w = {w}')
    
    # length of the low edge
    a = dist(wall1, shot_point)
    print(f'a = {a}')
    
    # length of the high edge
    b = dist(wall2, shot_point)
    print(f'b = {b}')
    
    # angle from shooting point, between wall1 (down) and wall2 (up)
    w_angle = angle(wall1, shot_point, wall2)
    print(f'w_angle = {w_angle}')
    
    # angle from shooting point, between wall1 (down) and second point
    lower_angle = angle(wall1, shot_point, later_point)
    print(f'lower_angle = {lower_angle}')
    
    # angle from shooting point, between second point and wall2 (up)
    upper_angle = angle(later_point, shot_point, wall2)
    print(f'upper_angle = {upper_angle}')
    
    # calculate the point where the bullet hits the wall
    alpha = angle(wall2, wall1, shot_point)
    print(f'alpha = {alpha}')
    beta = angle(wall1, wall2, shot_point)
    print(f'beta = {beta}')
    l = abs(b * sin(lower_angle) / sin(beta))
    print(f'l = {l}')
    gamma = 180 - beta - upper_angle
    print(f'gamma = {gamma}')
    u = abs(a * sin(upper_angle) / sin(gamma))
    print(f'u = {u}')
    
    
    
    # check if target is lower part of the wall
    if lower_angle == 0:
        return 0
    
    # check if target is upper part of the wall
    if upper_angle == 0:
        return 0
    
    # check if target is middle part of the wall
    
    
    # check if target is over the wall
    if lower_angle > w_angle:
        return -1
    
    # check the points


# Best Solution: 
# https://py.checkio.org/mission/shoot-range/publications/rodka81/python-3/sympygeometry/?ordering=most_voted&filtering=all

from sympy.geometry import intersection, Point, Line, Segment

def shot(wall1, wall2, shot_point, later_point):
    wall = Segment(wall1, wall2)
    trajectory = Line(shot_point, later_point)
    intersect = intersection(wall, trajectory)
    target = (Point(wall1) + Point(wall2)) / 2
    half_wall_length = Point(wall1).distance(wall2) / 2

    if Point(later_point).distance(target) > Point(shot_point).distance(target):
        return -1

    if len(intersect) == 1:
        return round(100 - intersect[0].distance(target)*100/half_wall_length)

    return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
    print('Done!!!')