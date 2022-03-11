'https://py.checkio.org/en/mission/the-healers/'

'''
Healer won't be fighting (his attack = 0, so he can't deal the damage). 
But his role is also very important - every time the allied soldier hits the enemy, the Healer will heal the allie, 
standing right in front of him by +2 health points with the heal() method. Note that the health after healing can't be greater than 
the maximum health of the unit. For example, if the Healer heals the Warrior with 49 health points, the Warrior will have 50 hp, 
because this is the maximum for him.
The basic parameters of the Healer:
health = 60
attack = 0
'''

# Best Solution: 
# https://py.checkio.org/mission/the-healers/publications/vperinova/python-3/second/?ordering=most_voted&filtering=all

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.following = 0
        self.health_max = self.health

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_hit(self, attack):
        self.health -= attack if attack <= self.health else self.health

    def heal(self, mate):
        pass

    def do_attack(self, enemy):
        enemy.take_hit(self.attack)
        if self.following:
            self.following.heal(self)


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.deffence = 2


    def take_hit(self, attack):
        super().take_hit(max(attack - self.deffence, 0))

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5

    def do_attack(self, enemy):
        h1 = enemy.health
        super().do_attack(enemy)
        h2 = enemy.health
        self.health += (h1 - h2) * self.vampirism


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6

    def do_attack(self, enemy):
        super().do_attack(enemy)
        if enemy.following:
            enemy.following.take_hit(self.attack // 2)


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 0
        self.cure = 2

    def heal(self, mate):
        mate.health = min(mate.health + self.cure, mate.health_max)


def fight(unit_1, unit_2):
    while True:
        if unit_1.is_alive:
            unit_1.do_attack(unit_2)
        else:
            return False
        if unit_2.is_alive:
            unit_2.do_attack(unit_1)
        else:
            return True


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit, count):
        for i in range(count):
            new_unit = unit()
            self.units.append(new_unit)
            if len(self.units) > 1:
                self.units[-2].following = new_unit


class Battle:
    def fight(self, army_1, army_2):
        while True:
            if fight(army_1.units[0], army_2.units[0]):  
                del army_2.units[0]
                if not army_2.units:
                    return True
            else:
                del army_1.units[0]
                if not army_1.units:
                     return False




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
    priest = Healer()

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
    assert freelancer.health == 14    
    priest.heal(freelancer)
    assert freelancer.health == 16

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")