'https://py.checkio.org/en/mission/interesting-intersecting/share/3573d4d22128e820dfea6e766880c843/'

'''
A square on the two-dimensional plane can be defined as a tuple (x, y, l), where (x, y) are the coordinates of 
its bottom left corner and l is the length of the side of the square (we only consider squares that are aligned to the axes). 
Given two squares as tuples (x1, y1, l1) and (x2, y2, l2), your function should determine whether these two squares intersect.
'''

# My Solution:

def squares_intersect_(s1: tuple[int, int, int], s2: tuple[int, int, int]) -> bool:
    '''
    top_left_1: Top Left coordinate of first square. 
    bottom_right_1: Bottom Right coordinate of first square. 
    top_left_2: Top Left coordinate of second square. 
    bottom_right_2: Bottom Right coordinate of second square.
    '''
    x1, y1, l1 = s1
    x2, y2, l2 = s2
    
    top_left_1_x = x1
    top_left_1_y = y1 + l1
    bottom_right_1_x = x1 + l1
    bottom_right_1_y = y1
    top_left_2_x = x2
    top_left_2_y = y2 + l2
    bottom_right_2_x = x2 + l2
    bottom_right_2_y = y2
    
    # If one square is on left side of other
    if (top_left_1_x > bottom_right_2_x) or (top_left_2_x > bottom_right_1_x):
        return False
    
    # If one square is above other
    if (bottom_right_1_y > top_left_2_y) or (bottom_right_2_y > top_left_1_y):
        return False
    
    return True


# Another Solution of mine:

from sympy import Polygon

def squares_intersect(s1: tuple[int, int, int], s2: tuple[int, int, int]) -> bool:
    x1, y1, l1 = s1
    m2, n2, l2 = s2
        
    p1, p2, p3, p4 = [(x1, y1 + l1), (x1 + l1, y1 + l1), (x1 + l1, y1), (x1, y1)]
    poly1 = Polygon(p1, p2, p3, p4)
    
    r1, r2, r3, r4 = [(m2, n2 + l2), (m2 + l2, n2 + l2), (m2 + l2, n2), (m2, n2)]
    poly2 = Polygon(r1, r2, r3, r4)
    
    if poly1.intersection(poly2) == []:
        return False
    else:
        return True


print("Example:")
#print(squares_intersect((2, 2, 3), (5, 5, 2)))

assert squares_intersect((2, 2, 3), (5, 5, 2)) == True
assert squares_intersect((3, 6, 1), (8, 3, 5)) == False
assert squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")