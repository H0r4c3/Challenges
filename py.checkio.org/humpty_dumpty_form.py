'https://py.checkio.org/en/mission/humpty-dumpty/'

'''
You can help him and create a function to calculate the volume (cubic inches) and the surface area (square inches).

Be careful with sin -1 x -- this is arcsin.

'''

from math import pi, sqrt, asin, atanh

def volume_of_ellipsoid(r1, r2, r3):
    return (4/3) * pi * r1 * r2 * r3


def surface_area_of_ellipsoid(height, width):
    if height == width:
        r = 0.5 * width
        surface_area = 4 * pi * r**2
        return surface_area
    
    elif height > width: #If ellipsoid is prolate 
        a = 0.5 * width
        b = 0.5 * height
        e2 = 1 - a**2 / b**2
        e = sqrt(e2) 
        surface_area = 2 * pi * a**2 * (1 + b / (a * e) * asin(e))
        return surface_area
    
    elif height < width: #If ellipsoid is oblate 
        a = 0.5 * width
        b = 0.5 * height
        e2 = 1 - b**2 / a**2
        e = sqrt(e2) 
        surface_area = 2 * pi * a**2 * (1 + (1 - e2) / e * atanh(e))
        return surface_area

def checkio(height, width):
    volume = volume_of_ellipsoid(0.5 * height, 0.5 * width, 0.5 * width)
    area = surface_area_of_ellipsoid(height, width)
    
    result = [round(volume, 2), round(area, 2)]
    print(result)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
    print('Done!!!')