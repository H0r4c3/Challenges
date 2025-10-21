'https://py.checkio.org/en/mission/oop-series-6/'

'''
6.1. Rewrite start_engine and stop_engine methods of the ElectricCar class to display another messages "Electric motor has started" and 
"Electric motor has stopped" respectively and change attributes the same way.

6.2. Call the start_engine method for the my_electric_car instance.

6.3. Create my_electric_car2 (values 60, "Toyota", "Prius"), start and stop its engine.
'''

# Taken from mission OOP 5: Parent - Child

class Car:
    # class attributes
    wheels = 'four'
    doors = 4
    working_engine = False
    
    # instance attributes
    def __init__(self, brand='', model=''):
        self.brand = brand
        self.model = model
        
    def start_engine(self):
        print('Engine has started')
        self.working_engine = True
    
    def stop_engine(self):
        print('Engine has stopped')
        self.working_engine = False
        
class ElectricCar(Car):
    def __init__(self, battery_capacity, brand='', model=''):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        
    def start_engine(self):
        print('Electric motor has started')
        self.working_engine = True
    
    def stop_engine(self):
        print('Electric motor has stopped')
        self.working_engine = False
    
my_car = Car()
some_car1 = Car('Ford', 'Mustang')
some_car2 = Car('', 'Camaro')
some_car1.start_engine()
some_car2.start_engine()

my_electric_car = ElectricCar(100, 'Tesla', 'Model 3')
my_electric_car.start_engine()

my_electric_car2 = ElectricCar(60, 'Toyota', 'Prius')
my_electric_car2.start_engine()
my_electric_car2.stop_engine()

