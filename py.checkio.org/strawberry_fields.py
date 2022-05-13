'https://py.checkio.org/en/mission/strawberry-fields/'

'''
The fence is made of 4 parts (a, b, c, d) and each of them has (but not necessarily) a different length. 
They are going to be placed around the field in a counterclockwise order.

It's up to you to write a function that returns (in degrees) the angle of the inside corner α which 
forms between the first and last part of the fence (a and d) so that the fence encloses the maximum area for our strawberry bed.

You are given four numbers (a, b, c, d) that represent the lengths of the four fence parts. 
Your function has to return the angle measured from the inside and formed in order to enclose the maximum area. 
The angle we are searching for should be rounded to one tenth of a degree
'''

from math import acos, pi

def strawberryfield(a, b, c, d):
    result = (a**2 + d**2 - b**2 - c**2) / (2 * (b*c + d*a))
    result = acos(result) / pi*180
    
    print(round(result, 1))
    return round(result, 1)



# Best Solution: 
# https://github.com/Darkhunter9/python/blob/master/Strawberry-fields.py

from math import acos, pi

def strawberryfield_(a, b, c, d):
    result = -(b**2 + c**2 - d**2 - a**2) / 2. / (b*c + d*a)
    result = acos(result) / pi*180
    return round(result, 1)



# These "asserts" are used for self-checking only and not for an auto-testing
if __name__ == '__main__':
    assert(strawberryfield(100, 100, 100, 100) == 90)  , "square"
    assert(strawberryfield(150, 100, 150, 100) == 90)  , "rectangle"   
    assert(strawberryfield(150, 100, 50, 100) == 60)   , "trapezium"
    assert(strawberryfield(203, 123, 82, 117) == 60.8) , "quadrilateral"
    
    print("Looks good so far! . . . How does 'Check' ?")