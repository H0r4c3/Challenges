'https://py.checkio.org/en/mission/area-of-a-convex-polygon/'

'''
There is a convex polygon on a coordinate plane. This polygon is presented as a list of vertices coordinates. 
Each vertex is connected sequentially with the last connecting back to the first. A polygon has N vertices. 
You should write a program that will calculate the area of a polygon. The result should be given with one digits precision as ±0.1.
'''

def checkio(data):
    # The algorithm is explained here: https://www.mathopenref.com/coordpolygonarea2.html
    
    area_x_2 = 0
    i = 0
    j = len(data) - 1

    for _ in data:
        xi = data[i][0]
        yi = data[i][1]
        xj = data[j][0]
        yj = data[j][1]
        area_x_2 += (xj + xi) * (yj - yi)
        j = i
        i += 1

    return abs(area_x_2 / 2)



if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
    print('Done!!!')