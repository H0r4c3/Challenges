'https://py.checkio.org/en/mission/capital-city/'

'''
Your task is to create the class Capital which has some special properties: the first created instance of this class will 
be unique and single, and all of the other instances should be the same as the very first one.
Also you should add the name() method which returns the name of the capital.
In this mission you should use the Singleton design pattern.
'''

        
class Capital:
    class _Capital:
        def __init__(self, city_name):
            self._name = city_name
            
        def name(self):
            return self._name
        
    city_name = None
    
    def __new__(self, city_name):
        if not self.city_name:
            self.city_name = self._Capital(city_name)
        return self.city_name
    
  
  

# Best Solution:
# https://py.checkio.org/mission/capital-city/publications/gileadslostson/python-3/first/share/6284202ab5f5393a7c23e366f469eade/


# class Capitalxxx:
#     class __Capital:
#         def __init__(self, city_name):
#             self._name = city_name
            
#         def name(self):
#             return self._name
    
#     instance = None
    
#     def __new__(self, city_name):
#         if not Capital.instance:
#             Capital.instance = Capital.__Capital(city_name)
#         return Capital.instance
 
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")
    print(ukraine_capital_2.name())

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"
    print(ukraine_capital_2)
    print(ukraine_capital_1)
    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")