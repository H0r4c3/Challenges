'https://py.checkio.org/en/mission/counting-tiles/'

'''
Each square tile has size of 1x1 meters. 
You need to calculate how many whole and partial tiles are needed for a circle with a radius of N meters. 
The center of the circle will be at the intersection of four tiles. 
For example: a circle with a radius of 2 metres requires 4 whole tiles and 12 partial tiles.
'''
from math import hypot, floor

def checkio(radius):
    whole = 0
    partial = 0
    max_tile = floor(radius) + 1
    
    for x in range(max_tile):
        for y in range(max_tile):
            if hypot(x + 1, y + 1) <= radius:
                whole += 1
            elif hypot(x, y) < radius:
                partial += 1
                
    # all tiles
    print([whole * 4, partial * 4])
    return [whole * 4, partial * 4] 




# Best Solution:
# https://py.checkio.org/mission/counting-tiles/publications/MichalMarsalek/python-3/second/share/067f9d9d77d83a60c0b54d66224c4b87/

import math

def checkio_(radius):
    solid = 0
    partial = 0
    n = math.floor(radius) + 1 #Max square coordinates evaulated
    for y in range(n):
        for x in range(n): #Iterates throught first quandrant
            if math.hypot(x+1, y+1) <= radius: #If top right corner is inside a circle
                solid += 1  #then whole square is inside a circle
            elif math.hypot(x, y) < radius: #If bottom left corner is inside a circle
                partial += 1 #then part of a square is inside a circle
    return [solid*4, partial*4] #Multiplies values by 4 to register all quadrants



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
    print('Done!!!')