'https://py.checkio.org/en/mission/geometry-figures/'

'''
You often work with the different geometrical figures and with their parameters - the perimeter, area, and volume. 
You are tired of doing it manually, so you’ve decided to automate this process, and therefore you need to write a particular program. 
In this program you should create the class Parameters which will choose one of the few figures 
(the circle, regular triangle, square, regular pentagon, regular hexagon, cube) using the choose_figure() method and will count the perimeter, 
area, and volume with the help of the following methods:

perimeter() - returns the perimeter of the figure;
area() - returns the area of the figure;
volume() - returns the volume of the figure.

Also you have to create a class for each figure and use the Strategy design pattern to solve this mission.
Every figure, except the cube, has the volume = 0.
If the result has no decimal places, you should return it as int(), in other case - round it to the 2 decimal points.
'''
from math import pi, tan

def rounding(f): 
    
    def wrapper(n):
        return round(f(n), 2)
    
    return wrapper
        

class Parameters:
    def __init__(self, dimension):
        self.dimension = dimension

    def choose_figure(self, figure):
        self.figure = figure

    @rounding
    def perimeter(self):
        return self.figure.perimeter(self.dimension)

    @rounding
    def area(self):
        return self.figure.area(self.dimension)

    @rounding
    def volume(self):
        return self.figure.volume(self.dimension)


class Circle:
    def perimeter(self, radius):
        return 2*pi*radius

    def area(self, radius):
        return pi*radius**2

    def volume(self, radius):
        return 0


class Polygon:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def perimeter(self, side):
        return  self.number_of_sides*side

    def area(self, side):
        return self.number_of_sides*side**2/4/tan(pi/self.number_of_sides)

    def volume(self, side):
        return 0


class Triangle(Polygon):
    def __init__(self):
        super().__init__(number_of_sides=3)


class Square(Polygon):
    def __init__(self):
        super().__init__(number_of_sides=4)


class Pentagon(Polygon):
    def __init__(self):
        super().__init__(number_of_sides=5)


class Hexagon(Polygon):
    def __init__(self):
        super().__init__(number_of_sides=6)


class Cube:
    def __init__(self):
        self.number_of_sides = 12
        self.number_of_faces = 6

    def perimeter(self, side):
        number_of_sides = 12
        return number_of_sides*side

    def area(self, side):
        return self.number_of_faces*side**2

    def volume(self, side):
        return side**3
    
    
    
    
# Best Solution: 
# https://py.checkio.org/mission/geometry-figures/publications/Sim0000/python-3/abc/share/e8b1dd3d55373a2b35705a35f617f222/

# from abc import ABC, abstractmethod
# from math import pi, sqrt

# class Parameters:
#     def __init__(self, *args):
#         self.args = args

#     def choose_figure(self, figure):
#         self.figure = figure

#     def perimeter(self):
#         return round(self.figure.perimeter(*self.args), 2)

#     def area(self):
#         return round(self.figure.area(*self.args), 2)

#     def volume(self):
#         return round(self.figure.volume(*self.args), 2)

# class Figure(ABC):
#     @abstractmethod
#     def perimeter(self, a):
#         pass

#     @abstractmethod
#     def area(self, a):
#         pass

#     def volume(self, a):
#         return 0

# class Circle(Figure):
#     perimeter = lambda self, a: 2 * pi * a
#     area = lambda self, a: pi * a**2

# class Triangle(Figure):
#     perimeter = lambda self, a: 3 * a
#     area = lambda self, a: sqrt(3) / 4 * a**2

# class Square(Figure):
#     perimeter = lambda self, a: 4 * a
#     area = lambda self, a: a**2

# class Pentagon(Figure):
#     perimeter = lambda self, a: 5 * a
#     area = lambda self, a: sqrt(25 + 10 * sqrt(5)) / 4 * a**2

# class Hexagon(Figure):
#     perimeter = lambda self, a: 6 * a
#     area = lambda self, a: 3 * sqrt(3) / 2 * a**2

# class Cube(Figure):
    # perimeter = lambda self, a: 12 * a
    # area = lambda self, a: 6 * a**2
    # volume = lambda self, a: a**3
    
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)
    
    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")