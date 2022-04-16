'https://github.com/thetufter/area_of_convex_polygon/blob/master/area_of_convex_polygon/function.py'


def area_of_convex_polygon(points):
    '''
    This function calculate the area of a convex polygon
    that represented by a (closed) list of points in cartesian space.
    The only argument is the list of points as a list/tuple of lists/tuples
    as the following format:
    [(x1, y1), (x2, y2), (x3, y3),...]
    Example:
    area_of_convex_polygon( [(0,0), (4,0), (4,4), (0,4)] )
    '''

    # Validate the input
    if not isinstance(points, (list, tuple)):
        raise TypeError('Invalid input: The polygon must be presented by a list or a tuple of points.')
    if len(points) < 3:
        raise ValueError('Invalid input: The polygon must have at least 3 points.')
    for point in points:
        if not isinstance(point, (list, tuple)):
            raise TypeError('Invalid input: Each point must be presented by a list or a tuple of 2 coordinates.')
        if len(point) != 2:
            raise ValueError('Invalid input: Each point must have 2 coordinates.')

    # Calculate the area using the following algorithm: https://www.mathopenref.com/coordpolygonarea2.html
    double_area = 0
    i = 0
    j = len(points) - 1

    for point in points:
        xi = points[i][0]
        yi = points[i][1]
        xj = points[j][0]
        yj = points[j][1]
        double_area += (xj + xi) * (yj - yi)
        j = i
        i += 1

    return abs(double_area / 2)


result = area_of_convex_polygon([[4, 1], [3, 4], [3, 7], [4, 8],
         [7, 9], [9, 6], [7, 1]])
print(result)