'https://py.checkio.org/en/mission/simple-areas/'

'''
You should write a function to calculate the area of simple figures: circles, rectangles and triangles. 
You are give an arbitrary number of arguments and depending on this, the function calculates area for the different figures.

One argument -- The diameter of a circle and you need calculate the area of the circle.
Two arguments -- The side lengths of a rectangle and you need calculate the area of the rectangle.
Three arguments -- The lengths of each side on a triangle and you need calculate the area of the triangle.

The result should be given with two digits precision as ±0.01.
'''
from math import pi

def simple_areas(*args):
    print(args)
    
    if len(args) == 1:
        area = pi * (args[0]/2)**2
        print(area)
        return area
    elif len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 3:
        a, b, c = args[0], args[1], args[2]
        s = (a + b + c) / 2
        
        # Heron's formula
        area = ((s - a) * (s - b) * (s - c) * s) ** (1/2)
        print(area)
        return(area)
    
    else:
        print('Unknown figure!')
        
    
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
    print('Done!!!')