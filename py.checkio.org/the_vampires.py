'https://py.checkio.org/en/mission/the-vampires/'

'''
Vampire should be the subclass of the Warrior class and have the additional vampirism parameter, which helps him to heal himself. 
When the Vampire hits the other unit, he restores his health by +50% of the dealt damage (enemy defense makes the dealt damage value lower).
The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%

You should store vampirism attribute as an integer (50 for 50%). 
It will be needed to make this solution evolutes to fit one of the next challenges of this saga.
'''

class Warrior:
    def __init__(self, health=50, attack=5, defense=0, vampirism=0) -> None:
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        
    def __str__(self):
        return f'{self.__class__.__name__}, health: {self.health}, attack: {self.attack}, defense: {self.defense}, vampirism: {self.vampirism}'
    
    @property    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)
        
        
class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3, defense=2)
        

class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=3, vampirism=50)

class Rookie(Warrior):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.health = 50
            self.attack = 1
        
        
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
        damage = unit_2.defense - unit_1.attack
        if damage >= 0:
            unit_2.health = unit_2.health + damage * unit_2.vampirism/100
        else:
            unit_2.health = unit_2.health - abs(damage) + abs(damage) * unit_2.vampirism/100
        print(f'{unit_2}')
        if unit_2.health <= 0:
            print(f'{unit_2} is dead')
            break
        else:
            # unit 2 attacks
            damage = unit_1.defense - unit_2.attack
            if damage >= 0:
                unit_1.health = unit_1.health
            else:
                unit_1.health = unit_1.health - abs(damage)
            print(f'{unit_1}')
            if unit_1.health <= 0:
                print(f'{unit_1} is dead')
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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")