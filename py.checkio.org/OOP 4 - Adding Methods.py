'https://py.checkio.org/en/mission/oop-series-4/'

'''
4.1. Add the working_engine class attribute inside the Car class and assign it a value of False.

4.2. Add a start_engine method to the Car class, that displays the message "Engine has started" and 
changes the working_engine value of the instance of class to True.

4.3. Add a stop_engine method to the Car class, that displays the message "Engine has stopped" and 
changes the working_engine value of the instance of class to False.

4.4. Call the start_engine method for both instances some_car1, some_car2.
'''

class Car:
    # class attributes
    wheels = 'four'
    doors = 4
    working_engine = False
    
    # instance attributes
    def __init__(self, brand='', model=''):
        self.brand = brand
        self.model = model
    
    # instance method    
    def start_engine(self):
        print('Engine has started')
        Car.working_engine = True
    
    # instance method
    def stop_engine(self):
        print('Engine has stopped')
        Car.working_engine = False
    
my_car = Car()

some_car1 = Car('Ford', 'Mustang')
some_car2 = Car('', 'Camaro')

some_car1.start_engine()
print(f'working_engine = {Car.working_engine}')
some_car1.stop_engine()
print(f'working_engine = {Car.working_engine}')

some_car2.start_engine()
print(f'working_engine = {Car.working_engine}')
some_car2.stop_engine()
print(f'working_engine = {Car.working_engine}')