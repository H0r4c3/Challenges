'https://py.checkio.org/en/mission/3-chefs/'

'''
You are the owner of a cafe where 3 chefs work: a JapaneseCook, RussianCook and ItalianCook. Each of them can prepare the national food and beverage:
- JapaneseCook: Sushi and Tea;
- RussianCook: Dumplings and Compote;
- ItalianCook: Pizza and Juice.
Your task is to create 3 different subclasses (one for each chef) which are the children of an AbstractCook and have these methods:
- add_food(food_amount, food_price), which add to the client's order the value of the food which he had chosen;
- add_drink(drink_amount, drink_price), which add to the client's order the value of the drink which he had chosen;
- total(), which returns a string like: 'Foods: 150, Drinks: 50, Total: 200', and for the each chef instead of the Foods and Drinks 
will be the national food and drink that he’s used.
Every client can choose only one chef. In this mission the Abstract Factory design pattern could help.
'''

class AbstractCook:
    def __init__(self):
        self.food_total = 0
        self.drink_total = 0

    def add_food(self, food_amount, food_price):
        self.food_total += food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.drink_total += drink_amount * drink_price

    def total(self):
        f = self.food_total
        d = self.drink_total
        return f'{self.food_name}: {f}, {self.drink_name}: {d}, Total: {f + d}'

class JapaneseCook(AbstractCook):
    food_name = 'Sushi' 
    drink_name = 'Tea'

class RussianCook(AbstractCook):
    food_name = 'Dumplings'
    drink_name = 'Compote'

class ItalianCook(AbstractCook):
    food_name = 'Pizza'
    drink_name = 'Juice'


# Best Solution: 
# https://py.checkio.org/mission/3-chefs/publications/flpo/python-3/abstractcook/share/14be50dbba75ffd7310797807039d871/


# class AbstractCook:
#     def __init__(self):
#         self.food_total = self.drink_total = 0

#     def add_food(self, food_amount, food_price):
#         self.food_total += food_amount * food_price

#     def add_drink(self, drink_amount, drink_price):
#         self.drink_total += drink_amount * drink_price

#     def total(self):
#         f, d = self.food_total, self.drink_total
#         return f'{self.food}: {f}, {self.drink}: {d}, Total: {f + d}'


# class JapaneseCook(AbstractCook):
#     food, drink = 'Sushi', 'Tea'

# class RussianCook(AbstractCook):
#     food, drink = 'Dumplings', 'Compote'

# class ItalianCook(AbstractCook):
#     food, drink = 'Pizza', 'Juice'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")