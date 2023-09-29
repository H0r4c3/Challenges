'https://py.checkio.org/en/mission/oop-series-5/'

'''
5.1. Create an ElectricCar class that inherits properties from the Car class.

5.2. Modify the __init__ method of the ElectricCar class so that it uses super() to call the __init__ method of the Car class.

5.3. Add a new attribute battery_capacity of type int to the ElectricCar class __init__ method. 
This attribute must be passing as argument. Put this argument before brand and model, because arguments without default values must go before ones that have.

5.4. Create a my_electric_car instance of the ElectricCar class, passing battery_capacity, brand, model with values 100, "Tesla", "Model 3" respectively.
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
    

class ElectricCar(Car):
    def __init__(self, battery_capacity, brand='', model=''):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        

my_electric_car = ElectricCar(100, 'Tesla', 'Model 3')
print(f'my_electric_car.battery_capacity = {my_electric_car.battery_capacity}')
print(f'my_electric_car.brand = {my_electric_car.brand}')
print(f'my_electric_car.model = {my_electric_car.model}')

my_electric_car.start_engine()
my_electric_car.stop_engine
    

