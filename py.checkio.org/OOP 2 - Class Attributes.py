'https://py.checkio.org/en/mission/oop-series-2/'

'''
2.1. Add the wheels class attribute inside the Car class and assign it a value of "four".

2.2. Add the doors class attribute inside the Car class and assign it a value of 4.
'''

class Car:
    # class attributes
    wheels = 'four'
    doors = 4
    
    # instance attributes
    def __init__(self):
        pass
    
my_car = Car()

print(f'my_car = {my_car}')
print(f'Car.wheels = {Car.wheels}')
print(f'Car.doors = {Car.doors}')
print(f'my_car.doors = {my_car.doors}')