'https://py.checkio.org/en/mission/the-lancers/'

'''
Lancer should be the subclass of the Warrior class and should attack in a specific way - when he do_damages the enemy unit, 
he also deals a 50% of the deal damage to the enemy unit, standing behind the firstly assaulted one (enemy defense makes the deal damage value lower - consider this).
The basic parameters of the Lancer:
health = 50
attack = 6

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
    
    def take_damage(self, attack):
        self.health -= self.damage(attack)
        
    def do_damage(self, enemy):
        enemy.take_damage(self.attack)
        
    def damage(self, attack):
        return attack
        
        
class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)
        
class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2
        
    def damage(self, attack):
        return max(0, attack - self.defense)
        
class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.vampirism = 50
        
    def do_damage(self, enemy):
        super().do_damage(enemy)
        self.health += enemy.damage(self.attack) * self.vampirism // 100
        
        
class Lancer(Warrior):
    def __init__(self):
        super().__init__(health=50, attack=6)
        

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
    while 1:
        # unit 1 attacks
        unit_1.do_damage(unit_2)
        print(f'{unit_2}')
        if unit_2.health <= 0:
            print(f'{unit_2} is dead')
            return True
        # unit 2 attacks
        unit_2.do_damage(unit_1)
        print(f'{unit_1}')
        if unit_1.health <= 0:
            print(f'{unit_1} is dead')
            return False
               
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
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
