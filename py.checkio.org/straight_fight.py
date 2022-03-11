'https://py.checkio.org/en/mission/straight-fight/'

'''
A new unit type won’t be added in this mission, but instead we’ll add a new tactic - straight_fight(army_1, army_2). 
It should be the method of the Battle class and it should work as follows:
at the beginning there will be a few duels between each pair of soldiers from both armies (the first unit against the first, 
the second against the second and so on). After that all dead soldiers will be removed and the process repeats until all soldiers 
of one of the armies will be dead. Armies might not have the same number of soldiers. If a warrior doesn’t have an opponent from the 
enemy army - we’ll automatically assume that he’s won a duel (for example - 9th and 10th units from the first army, if the second has only 8 soldiers).
'''



# Best Solution: 
# https://py.checkio.org/mission/straight-fight/publications/Moff/python-3/first/share/fa81d5884444faace906236a5b53f0d5/

class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other):
        other.loss(self.attack)

    def damage(self, attack):
        return attack

    def loss(self, attack):
        self.health -= self.damage(attack)


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

    def hit(self, other):
        super().hit(other)
        self.health += other.damage(self.attack) * self.vampirism // 100


class Lancer(Warrior):
    def __init__(self):
        super().__init__(attack=6)


class Healer(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=0)
        self.heal_rate = 2

    def heal(self, other):
        other.health += self.heal_rate


def fight(unit_1, unit_2):
    while 1:
        unit_1.hit(unit_2)
        if unit_2.health <= 0:
            return True
        unit_2.hit(unit_1)
        if unit_1.health <= 0:
            return False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, count):
        for _ in range(count):
            self.units.append(unit_class())

    @property
    def first_alive_unit(self):
        for unit in self.units:
            if unit.is_alive:
                return unit

    def next_unit(self, unit):
        i = self.units.index(unit)
        if i + 1 < len(self.units):
            return self.units[i + 1]

    @property
    def is_alive(self):
        return self.first_alive_unit is not None

    @property
    def alive_units(self):
        return [u for u in self.units if u.is_alive]


class Battle:
    @staticmethod
    def hit(army_1, army_2):
        unit_1 = army_1.first_alive_unit
        unit_2 = army_2.first_alive_unit

        unit_22 = army_2.next_unit(unit_2)
        unit_1.hit(unit_2)
        if unit_22 and isinstance(unit_1, Lancer):
            unit_22.loss(unit_1.attack // 2)

        unit_12 = army_1.next_unit(unit_1)
        if unit_12 and isinstance(unit_12, Healer):
            unit_12.heal(unit_1)

    @classmethod
    def fight(cls, army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            unit_1 = army_1.first_alive_unit
            unit_2 = army_2.first_alive_unit
            while 1:
                cls.hit(army_1, army_2)
                if unit_2.health <= 0:
                    break
                cls.hit(army_2, army_1)
                if unit_1.health <= 0:
                    break
        return army_1.is_alive

    @classmethod
    def straight_fight(cls, army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            for unit_1, unit_2 in zip(army_1.alive_units, army_2.alive_units):
                fight(unit_1, unit_2)
        return army_1.is_alive



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

    army_5 = Army()
    army_5.add_units(Warrior, 10)

    army_6 = Army()
    army_6.add_units(Warrior, 6)
    army_6.add_units(Lancer, 5)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    assert battle.straight_fight(army_5, army_6) == False
    print("Coding complete? Let's try tests!")