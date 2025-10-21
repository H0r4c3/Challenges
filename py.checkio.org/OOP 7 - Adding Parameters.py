'https://py.checkio.org/en/mission/oop-series-7-2/'

'''
7.1. Add the fuel_used attribute inside __init__ method of Car class without changing its arguments and assign it a value of 0 liters.

7.2. Add the fuel_consumption attribute inside __init__ method of Car class, passing it as a method argument with default value of 7 (liters/100 km).

7.3. Add a drive method to the Car class that takes the distance argument of type int (km). If an instance of class had started - increment 
fuel_used with the proper value ( that is based on fuel_consumption variable and distance parameter values) and display the 
message "Currently driven {distance} km, total fuel used - {fuel_used} l". If the instance had not started, display "Start the car before driving!". .

7.4. Rewrite the method for the ElectricCar class, add and do not increment fuel_used (since electric car doesn't used fuel), change the 
successful message to "Currently driven {distance} km on electric motor", keep the unsuccessful message unchanged.
'''

class Car:
    # class attributes
    wheels = 'four'
    doors = 4
    working_engine = False
    
    # instance attributes
    def __init__(self, brand='', model='', fuel_consumption = 7):
        self.brand = brand
        self.model = model
        self.fuel_used = 0
        self.fuel_consumption = fuel_consumption
        
    def start_engine(self):
        print('Engine has started')
        self.working_engine = True
    
    def stop_engine(self):
        print('Engine has stopped')
        self.working_engine = False
        
    def drive(self, distance):
        if self.working_engine:
            self.fuel_used += self.fuel_consumption * distance / 100
            print(f'Currently driven {distance} km, total fuel used - {self.fuel_used} l')
        else:
            print('Start the car before driving!')
        
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
        
    def drive(self, distance):
        if self.working_engine:
            print(f'Currently driven {distance} km on electric motor')
        else:
            print('Start the car before driving!')
    
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

# Test
test_car = Car()
test_car.start_engine()
test_car.drive(21)
test_car.drive(10)

#answer="Engine has started\nCurrently driven 21 km, total fuel used - 1.47 l\nCurrently driven 10 km, total fuel used - 2.17 l\n"