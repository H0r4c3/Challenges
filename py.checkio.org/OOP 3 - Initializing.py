'https://py.checkio.org/en/mission/oop-series-3/'

'''
3.1. Add an __init__() function to the Car class that takes the brand and model arguments and assigns them to the appropriate object attributes.

3.2. You already have an object my_car that was created without passing additional arguments. 
So, in order not to cause errors when creating an object in this way, let's add a default value for the arguments of the __init__() function 
They mast have values of empty string "".

3.3. Create two new Car objects by passing the following string values as arguments. some_car1: brand - Ford, model - Mustang; some_car2: model - Camaro. 
Notice, that the second car has only model, it's brand must remains default.
'''

class Car:
    # class attributes
    wheels = 'four'
    doors = 4
    
    # instance attributes
    def __init__(self, brand='', model=''):
        self.brand = brand
        self.model = model
    
my_car = Car()

some_car1 = Car('Ford', 'Mustang')
some_car2 = Car('', 'Camaro')

print(f'some_car2.brand = {some_car2.brand}')
print(f'some_car2.model = {some_car2.model}')