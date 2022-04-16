'https://py.checkio.org/en/mission/building-base/'

'''
To complete this mission we need to use a couple of operations. See the class description below.

class Building (south, west, width_WE, width_NS, height=10)

Returns a new Building instance with the South-West corner at [ south , west ] coordinates, the size 
is width_WE by width_NS and the height of the building is height . "height" is a positive number with a default value of 10.
'''

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        corners_dict = dict()
        corners_dict["north-west"] = [self.south + self.width_NS, self.west]
        corners_dict["north-east"] = [self.south + self.width_NS, self.west + self.width_WE]
        corners_dict["south-west"] = [self.south, self.west]
        corners_dict["south-east"] = [self.south, self.west + self.width_WE]
        
        #return {"north-west": [self.south + self.width_NS, self.west], "north-east": [self.south + self.width_NS, self.west + self.width_WE], "south-west": [self.south, self.west], "south-east": [self.south, self.west + self.width_WE]}
        return corners_dict

    def area(self):
        return self.width_NS * self.width_WE

    def volume(self):
        return self.width_NS * self.width_WE * self.height

    def __repr__(self):
        return f'Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})'
        



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
    print('Done!!!')