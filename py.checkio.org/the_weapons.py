'https://py.checkio.org/en/mission/the-weapons/'

'''
In this mission you should create a new class Weapon(health, attack, defense, vampirism, heal_power) which will equip your soldiers with weapons. 
Every weapon's object will have the parameters that will show how the soldier's characteristics change while he uses this weapon.

The parameters list:
health - add to the current health and the maximum health of the soldier this modificator;
attack - add to the soldier's attack this modificator;
defense - add to the soldier's defense this modificator;
vampirism - increase the soldier’s vampirism to this number (in %. So vampirism = 20 means +20%);
heal_power - increase the amount of health which the healer restore for the allied unit.

All parameters could be positive or negative, so when a negative modificator is being added to the soldier’s stats, 
they are decreasing, but none of them can be less than 0.
'''


class Warrior:
    def __init__(self, health=50, attack=5, defense=0, vampirism=0, heal_power=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power
        self.max_health = health

    @property
    def is_alive(self):
        return self.health > 0

    def heal(self, other):
        other.health = min(other.health + self.heal_power, other.max_health)

    def equip_weapon(self, weapon):
        self.max_health += weapon.health
        self.health += weapon.health
        self.attack += weapon.attack
        if self.defense>0:
            self.defense += weapon.defense
        if self.vampirism>0:
            self.vampirism += weapon.vampirism
        if self.heal_power>0:
            self.heal_power += weapon.heal_power


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.vampirism = 50


class Lancer(Warrior):
    def __init__(self):
        super().__init__(attack=6)


class Healer(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=0)
        self.heal_power = 2

class Weapon():
    def __init__(self, health=0, attack=0, defense=0, vampirism=0, heal_power=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power

class Sword(Weapon):
    def __init__(self):
        super().__init__(health=5,attack=2)
class Shield(Weapon):
    def __init__(self):
        super().__init__(health=20,attack=-1,defense=2)
class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(health=-15,attack=5,defense=-2,vampirism=10)
class Katana(Weapon):
    def __init__(self):
        super().__init__(health=-20,attack=6,defense=-5,vampirism=50)
class MagicWand(Weapon):
    def __init__(self):
        super().__init__(health=30,attack=3,heal_power=3)



class Army(list):
    def __init__(self):
        self.units = []

    def add_units(self, unit, n):
        self.extend(unit() for _ in range(n))
        self.units = self

class Battle:
    def fight(self, army_1, army_2):
        while army_1:
            if fight(army_1[0], army_2[0], army_1, army_2):
                del army_2[0]
            else:
                del army_1[0]
            if not army_2:
                return True
        return False

    def straight_fight(self, army_1, army_2):
        while army_1 and army_2:
            for x in zip(army_1, army_2):
                fight(x[0], x[1])
            army_1 = [x for x in army_1 if x.is_alive]
            army_2 = [x for x in army_2 if x.is_alive]
        return bool(army_1)


def fight(unit_1, unit_2, army_1=None, army_2=None):
    def hit(unit_1, unit_2, army_1, army_2):
        damage = max(0, unit_1.attack - unit_2.defense)
        unit_2.health -= damage

        unit_1.health = min(unit_1.health + int(damage * unit_1.vampirism / 100),unit_1.max_health)
        if isinstance(unit_1, Lancer) and army_2 is not None and len(army_2) > 1:
            army_2[1].health -= 0.5 * damage
        if army_1 is not None and len(army_1) > 1:
            army_1[1].heal(unit_1)

    while unit_1.is_alive:
        hit(unit_1, unit_2, army_1, army_2)
        if not unit_2.is_alive:
            return True
        hit(unit_2, unit_1, army_2, army_1)
    return False





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
	ogre = Warrior()
	lancelot = Knight()
	richard = Defender()
	eric = Vampire()
	freelancer = Lancer()
	priest = Healer()

	sword = Sword()
	shield = Shield()
	axe = GreatAxe()
	katana = Katana()
	wand = MagicWand()
	super_weapon = Weapon(50, 10, 5, 150, 8)

	ogre.equip_weapon(sword)
	ogre.equip_weapon(shield)
	ogre.equip_weapon(super_weapon)
	lancelot.equip_weapon(super_weapon)
	richard.equip_weapon(shield)
	eric.equip_weapon(super_weapon)
	freelancer.equip_weapon(axe)
	freelancer.equip_weapon(katana)
	priest.equip_weapon(wand)
	priest.equip_weapon(shield)

	ogre.health == 125
	lancelot.attack == 17
	richard.defense == 4
	eric.vampirism == 200
	freelancer.health == 15
	priest.heal_power == 5

	fight(ogre, eric) == False
	fight(priest, richard) == False
	fight(lancelot, freelancer) == True

	my_army = Army()
	my_army.add_units(Knight, 1)
	my_army.add_units(Lancer, 1)

	enemy_army = Army()
	enemy_army.add_units(Vampire, 1)
	enemy_army.add_units(Healer, 1)

	my_army.units[0].equip_weapon(axe)
	my_army.units[1].equip_weapon(super_weapon)

	enemy_army.units[0].equip_weapon(katana)
	enemy_army.units[1].equip_weapon(wand)

	battle = Battle()

	battle.fight(my_army, enemy_army) == True
	print("Coding complete? Let's try tests!")