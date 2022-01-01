'https://py.checkio.org/en/mission/army-battles/'

'''
The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the army. 

Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
'''

class Warrior:
    def __init__(self, health=50, attack=5) -> None:
        self.health = health
        self.attack = attack
        
    def __str__(self):
        return f'{self.__class__.__name__}, health: {self.health}, attack: {self.attack}'
    
    @property    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)

        

class Army:
    def __init__(self) -> None:
        self.list_of_units = []
    
    def add_units(self, unit, number):
        for _ in range(number):
            self.list_of_units.append(unit())
            
    def dead_unit(self):
        self.list_of_units.pop()
    

class Battle:
    def __init__(self) -> None:
        pass
    
    def fight(self, army_1, army_2):
        while len(army_1.list_of_units) > 0:

            if fight(army_1.list_of_units[-1], army_2.list_of_units[-1]):
                army_2.dead_unit()
            else:
                army_1.dead_unit()
            if len(army_2.list_of_units) == 0:
                return True

        return False
        


def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        # unit 1 attacks
        unit_2.health -= unit_1.attack
        #print(unit_2.health)
        if unit_2.health <= 0:
            break
        else:
            # unit 2 attacks
            unit_1.health -= unit_2.attack
            #print(unit_1.health)
            if unit_1.health <= 0:
                break
            
        
    if unit_1.is_alive:
        return True
    elif unit_2.is_alive:
        return False
    else:
        print('Draw')

      
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    
    

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False


    #warrior = Warrior()
    #knight = Knight()

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)
    

    battle = Battle()
    

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")