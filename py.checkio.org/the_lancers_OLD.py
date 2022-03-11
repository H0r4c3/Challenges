'https://py.checkio.org/en/mission/the-lancers/'

'''
Lancer should be the subclass of the Warrior class and should attack in a specific way - when he hits the other unit, 
he also deals a 50% of the deal damage to the enemy unit, standing behind the firstly assaulted one (enemy defense makes the deal damage value lower - consider this).
The basic parameters of the Lancer:
health = 50
attack = 6

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
        
        
# Best Solution: 
# https://py.checkio.org/mission/the-lancers/publications/mortonfox/python-3/first/share/5ce66abb7895fa35746494ee11b7f7bc/

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def take_hit(self, hit):
        self.health -= hit
        return hit

    def do_attack(self, other1, other2 = None, **options):
        hit = options.get('hit', self.attack)
        return other1.take_hit(hit)

class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 6

    def do_attack(self, other1, other2 = None, **options):
        damage = super().do_attack(other1)
        damage2 = super().do_attack(other2, None, hit = damage / 2) if other2 else 0
        return damage + damage2

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5

    def do_attack(self, other1, other2 = None, **options):
        damage = super().do_attack(other1)
        self.health += damage * self.vampirism
        return damage

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

    def take_hit(self, hit):
        return super().take_hit(max(0, hit - self.defense))

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    while True:
        unit_1.do_attack(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.do_attack(unit_1)
        if not unit_1.is_alive:
            return False

class Army:
    def __init__(self):
        self.units = []

    def add_units(self, klass, count):
        for i in range(count):
            self.units.append(klass())

    def cleanup(self):
        front_warrior_dead = self.units and not self.units[0].is_alive
        self.units = [u for u in self.units if u.is_alive]
        return front_warrior_dead

    def all_dead(self):
        return self.units == []

class Battle:
    def fight(self, army1, army2):
        army1_turn = True
        while not army1.all_dead() and not army2.all_dead():
            if army1_turn:
                army1.units[0].do_attack(*army2.units[:2])
            else:
                army2.units[0].do_attack(*army1.units[:2])
            army1_turn = not army1_turn

            front_warrior_dead1 = army1.cleanup()
            front_warrior_dead2 = army2.cleanup()
            if front_warrior_dead1 or front_warrior_dead2:
                # If front warrior died, always restart battle with first army.
                army1_turn = True

        return army2.all_dead()
    
    
    
# Best Solution
# https://py.checkio.org/mission/the-lancers/publications/mortonfox/python-3/first/share/5ce66abb7895fa35746494ee11b7f7bc/

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def take_hit(self, hit):
        self.health -= hit
        return hit

    def do_attack(self, other1, other2 = None, **options):
        hit = options.get('hit', self.attack)
        return other1.take_hit(hit)

class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 6

    def do_attack(self, other1, other2 = None, **options):
        damage = super().do_attack(other1)
        damage2 = super().do_attack(other2, None, hit = damage / 2) if other2 else 0
        return damage + damage2

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5

    def do_attack(self, other1, other2 = None, **options):
        damage = super().do_attack(other1)
        self.health += damage * self.vampirism
        return damage

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

    def take_hit(self, hit):
        return super().take_hit(max(0, hit - self.defense))

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    while True:
        unit_1.do_attack(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.do_attack(unit_1)
        if not unit_1.is_alive:
            return False

class Army:
    def __init__(self):
        self.units = []

    def add_units(self, klass, count):
        for i in range(count):
            self.units.append(klass())

    def cleanup(self):
        front_warrior_dead = self.units and not self.units[0].is_alive
        self.units = [u for u in self.units if u.is_alive]
        return front_warrior_dead

    def all_dead(self):
        return self.units == []

class Battle:
    def fight(self, army1, army2):
        army1_turn = True
        while not army1.all_dead() and not army2.all_dead():
            if army1_turn:
                army1.units[0].do_attack(*army2.units[:2])
            else:
                army2.units[0].do_attack(*army1.units[:2])
            army1_turn = not army1_turn

            front_warrior_dead1 = army1.cleanup()
            front_warrior_dead2 = army2.cleanup()
            if front_warrior_dead1 or front_warrior_dead2:
                # If front warrior died, always restart battle with first army.
                army1_turn = True

        return army2.all_dead()



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
