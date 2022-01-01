'https://py.checkio.org/en/mission/the-warriors/'

'''
You need to create the class Warrior , the instances of which will have 2 parameters - health (equal to 50 points) and 
attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case). 
In addition you have to create the second unit type - Knight, which should be the subclass of the Warrior but have the increased attack - 7. 
Also you have to create a function fight() , which will initiate the duel between 2 warriors and define the strongest of them. 
The duel occurs according to the following principle:
Every turn, the first warrior will hit the second and this second will lose his health in the same value as the attack of the first warrior. 
After that, if he is still alive, the second warrior will do the same to the first one.
The fight ends with the death of one of them. If the first warrior is still alive (and thus the other one is not anymore), the function should return True , 
False otherwise.

Input: The warriors.

Output: The result of the duel (True or False).
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
        


def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        # unit 1 attacks
        unit_2.health -= unit_1.attack
        print(unit_2.health)
        if unit_2.health <= 0:
            break
        else:
            # unit 2 attacks
            unit_1.health -= unit_2.attack
            print(unit_1.health)
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

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    
    #fight(chuck, bruce)
    
    print(f'chuck.health: {chuck.health}')
    print(f'bruce.health: {bruce.health}')
    print(chuck.is_alive)

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False