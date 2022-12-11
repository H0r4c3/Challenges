'https://py.checkio.org/en/mission/inside-block/'

'''
Input: Two arguments. Polygon coordinates as a tuple of tuples with two integers each. 
A checking point coordinates as a tuple of two integers.

Output: Whatever the point inside the polygon or not as a boolean.
'''

# My Solution (The module `shapely.geometry` is not allowed on checkio.)

from typing import Tuple
from shapely.geometry import Point, Polygon

def area_of_triangle(x1, y1, x2, y2, x3, y3):
    '''
    Calculate the area of triangle
    '''
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def is_inside_triangle(x1, y1, x2, y2, x3, y3, x, y):
    '''
    A function to check whether point P(x, y)
    lies inside the triangle formed by
    A(x1, y1), B(x2, y2) and C(x3, y3)
    '''
    # Calculate area of triangle ABC
    A = area_of_triangle(x1, y1, x2, y2, x3, y3)
 
    # Calculate area of triangle PBC
    A1 = area_of_triangle(x, y, x2, y2, x3, y3)
     
    # Calculate area of triangle PAC
    A2 = area_of_triangle(x1, y1, x, y, x3, y3)
     
    # Calculate area of triangle PAB
    A3 = area_of_triangle(x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3 is same as A
    if A == A1 + A2 + A3:
        return True
    else:
        return False
    
    
def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    if len(polygon) == 3:
        return is_inside_triangle(polygon[0][0], polygon[0][1], polygon[1][0], polygon[1][1], polygon[2][0], polygon[2][1], point[0], point[1])
        
    
    p1 = Point(point)
    poly1 = Polygon(polygon)
    
    result1 = p1.within(poly1)
    print(result1)
    
    #result2 = poly1.contains(p1)
    #print(result2)
     
    return result1
    #return result2



# Best Solution: 
# https://py.checkio.org/mission/inside-block/publications/jtokaz/python-3/first/share/55476cca956c3131a0e86b48125b887f/

def is_inside_(polygon, point):
  
  # shift polygon so that point is origin
  polygon = [(p[0]-point[0],p[1]-point[1]) for p in polygon]
  
  cnt = 0 # count number of segments crossing positive x-axis
  for i,p1 in enumerate(polygon):
    p2 = polygon[(i+1)%len(polygon)]
    if p2[1]*p1[1] <= 0: # crosses x axis, different y signs
      if p1[1]==0==p2[1]: # both y-coords 0
        if p1[0]>=0 or p2[0]>=0:
          return True
      else:
        x_int = p2[0] - p2[1]*(p2[0]-p1[0])/(p2[1]-p1[1])
        if x_int == 0:
          return True
        elif x_int > 0:
          cnt = cnt + 1
    for (u,v) in ((p1,p2),(p2,p1)):
      if u[1] == 0 and u[0] >= 0 and u[1] > v[1]:
        cnt = cnt + 1
  
  return cnt%2==1


if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (2, 2)) is True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (4, 2)) is False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)), (3, 2)) is True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)), (3, 3)) is False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)), (4, 3)) is True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)), (4, 3)) is False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)), (3, 3)) is True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)), (4, 3)) is False, "Eighth"
    print("All done! Let's check now")