''

'''
In this mission you should add a new class Warlord(), which should be the subclass of the Warrior class and have the next characteristics:
health = 100
attack = 4
defense = 2

Also, when the Warlord is included in any of the armies, that particular army gets the new move_units() method which allows to rearrange the 
units of that army for the better battle result. The rearrangement is done not only before the battle, but during the battle too, each time the allied units die. 
The rules for the rearrangement are as follow:
If there are Lancers in the army, they should be placed in front of everyone else.
If there is a Healer in the army, he should be placed right after the first soldier to heal him during the fight. If the number of Healers is > 1, all of them 
should be placed right behind the first Healer.
If there are no more Lancers in the army, but there are other soldiers who can deal damage, they also should be placed in first position, and the Healer should stay in the 2nd row (if army still has Healers).
Warlord should always stay way in the back to look over the battle and rearrange the soldiers when it's needed.
Every army can have no more than 1 Warlord.
If the army doesn’t have a Warlord, it can’t use the move_units() method.
'''



# Best Solution: 
# https://py.checkio.org/mission/the-warlords/publications/bsquare/python-3/clean-oop-solution-with-full-inheritance/share/a1d793384cf6e46c7a88bfc69c2a83a2/


from math import floor

def debug(_):
    pass

class Weapon:
    def __init__(self, health, attack, defense=0, vampirism=0, heal_power=0):
        self.health = self.max_health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power

class Sword(Weapon):
    def __init__(self):
        super().__init__(health=5, attack=2)

class Shield(Weapon):
    def __init__(self):
        super().__init__(health=20, attack=-1, defense=2)

class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(health=-15, attack=5, defense=-2, vampirism=10)

class Katana(Weapon):
    def __init__(self):
        super().__init__(health=-20, attack=6, defense=-5, vampirism=50)

class MagicWand(Weapon):
    def __init__(self):
        super().__init__(health=30, attack=3, heal_power=3)

class Warrior:
    _max_health = 50

    def __init__(self, attack=5):
        self._army = None
        self._weapons = []
        self.health = self._max_health
        self._attack = attack

    def join_army(self, army):
        self._army = army
        return self

    @property
    def max_health(self):
        return self._max_health + sum([weapon.max_health for weapon in self._weapons])

    @property
    def attack(self):
        return max(0, self._attack + sum([weapon.attack for weapon in self._weapons]))

    @attack.setter
    def attack(self, new_attack):
        self._attack = new_attack

    @property
    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, weapon):
        self._weapons.append(weapon)
        self.health = max(0, self.health + weapon.health)

    def hit(self, targets, specific_damage=None):
        # In this implementation targets is the list of all living opponents,
        #  by default, we still keep figthing only the first one.
        target = targets[0]

        # Optional specific_damage can be specified (when the lancer is hitting the 'next unit'.
        removed_health = target.damage_taken(specific_damage if specific_damage is not None else self.attack)
        target.update_health(-removed_health)

        return removed_health

    def damage_taken(self, attack):
        return attack

    def heal_received(self, heal_strength):
        # An unit can't be healed higher than its maximum health.
        return min(self.max_health - self.health, heal_strength)

    def update_health(self, update):
        self.health = min(self.max_health, self.health + update)

        if not self.is_alive and self._army is not None:
            self._army.notify_dead_warrior(self)

    def __str__(self):
        return f"Type={self.__class__.__name__}; Health={self.health}; Attack={self.attack}"

class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)

class Defender(Warrior):
    _max_health = 60

    def __init__(self, attack=3, defense=2):
        super().__init__(attack=attack)
        self._defense = defense

    @property
    def defense(self):
        return max(0, self._defense + sum([weapon.defense for weapon in self._weapons]))

    def damage_taken(self, attack):
        return max(0, attack - self.defense)

    def __str__(self):
        return super().__str__() + f"; Defense={self.defense}"

class Vampire(Warrior):
    _max_health = 40

    def __init__(self):
        super().__init__(attack=4)
        self._vampirism = 50

    @property
    def vampirism(self):
        return max(0, self._vampirism + sum([weapon.vampirism for weapon in self._weapons]))

    def hit(self, targets, specific_damage=None):
        removed_health = super().hit(targets)
        self.update_health(floor(self.vampirism * removed_health / 100))

    def __str__(self):
        return super().__str__() + f"; Vampirism={self.vampirism}"

class Lancer(Warrior):
    def __init__(self):
        super().__init__(attack=6)

    def hit(self, targets, specific_damage=None):
        # The hit is the same than usual, with the first opponent.
        removed_health = super().hit(targets)

        # If there is another opponent "behind", deals half of the same damage
        # Because we call the same method hit, the characteristic of the opponent
        #  will be taken care (like defense of a Defenseur).
        if len(targets) > 1:
            additional_damage = removed_health // 2
            # Important: the first argument MUST be a list, even if there is only one warrior.
            super().hit([targets[1]], specific_damage=additional_damage)

class Healer(Warrior):
    _max_health = 60

    def __init__(self):
        super().__init__(attack=0)
        self._heal_power = 2

    @property
    def heal_power(self):
        return max(0, self._heal_power + sum([weapon.heal_power for weapon in self._weapons]))

    def heal(self, target):
        heal_received = target.heal_received(self.heal_power)
        target.update_health(heal_received)

    def hit(self, targets, specific_damage=None):
        pass

    def __str__(self):
        return super().__str__() + f"; Heal_power={self.heal_power}"


class Warlord(Defender):
    _max_health = 100

    def __init__(self):
        super().__init__(attack=4, defense=2)


class Army:
    army_number = 0

    def __init__(self):
        Army.army_number += 1
        self._army_number = Army.army_number
        self.warriors = []

    @property
    def units(self):
        return self.warriors

    def add_units(self, cls, unit_count):
        # An army can only have one Warlord at most.
        if cls == Warlord:
            if any(filter(lambda unit: isinstance(unit, Warlord), self.warriors)):
                return
            unit_count = 1

        for _ in range(unit_count):
            self.warriors.append(cls().join_army(self))

    def __extract_specific_units(self, unit_cls):
        return [unit for unit in self.warriors if isinstance(unit, unit_cls)]

    def can_move_units(self):
        return self.__extract_specific_units(Warlord)

    def move_units(self):
        # Cleans dead warriors.
        self.warriors = self.next_living_warriors()

        warlord = self.__extract_specific_units(Warlord)
        if not warlord:
            return

        lancers = self.__extract_specific_units(Lancer)
        healers = self.__extract_specific_units(Healer)
        others = [unit for unit in self.warriors if not isinstance(unit, Warlord) and not isinstance(unit, Lancer) and not isinstance(unit, Healer)]

        new_ordered_units = lancers or others
        new_ordered_units[1:1] = healers
        if lancers:
            new_ordered_units.extend(others)
        new_ordered_units.extend(warlord)

        self.warriors = new_ordered_units

    def notify_dead_warrior(self, warrior):
        debug(f'DEAD in Army #{self._army_number}: {warrior}')
        self.move_units()

    def next_living_warriors(self):
        # In this implementation, we return ALL living warriors, in case interaction
        #  must be done with 'next unit' of the figthing one.
        return [unit for unit in self.warriors if unit.is_alive]

    def head_unit(self):
        living_unit = self.next_living_warriors()
        return living_unit[0] if living_unit else None

    def head_unit_healer(self):
        '''
            Returns the second unit if exists, and is a Healer.
        '''
        living_unit = self.next_living_warriors()
        return living_unit[1] if len(living_unit) > 1 and isinstance(living_unit[1], Healer) else None

    def is_destroyed(self):
        return not [unit for unit in self.warriors if unit.is_alive]

    def __str__(self):
        return f"Army #{self._army_number}: " + "; ".join([f"({unit})" for unit in self.warriors])

class Battle:
    def __init__(self):
        pass

    def fight(self, army_1: Army, army_2: Army):
        army_1.move_units()
        army_2.move_units()

        while not army_1.is_destroyed() and not army_2.is_destroyed():
            turn = 0
            while True:
                turn += 1
                debug(f' {army_1}\n {army_2}')

                attacking_army = (army_1, army_2)[not turn%2]
                target_army = (army_1, army_2)[turn%2]

                attacking_unit = attacking_army.head_unit()
                target_unit = target_army.head_unit()
                attacking_unit.hit(target_army.next_living_warriors())
                attacking_unit_healer = attacking_army.head_unit_healer()
                if attacking_unit_healer:
                    attacking_unit_healer.heal(attacking_unit)

                if not target_unit.is_alive:
                    break

        debug(f'FINAL\n {army_1}\n {army_2}')

        # Returns True or False, according to living unit in army_1 or not.
        return not army_1.is_destroyed()

    def straight_fight(self, army_1: Army, army_2: Army):
        army_1.move_units()
        army_2.move_units()

        while not army_1.is_destroyed() and not army_2.is_destroyed():
            units_1: list(Warrior) = army_1.next_living_warriors()
            units_2: list(Warrior) = army_2.next_living_warriors()

            debug(f' {army_1}\n {army_2}')

            for unit_1, unit_2 in zip(units_1, units_2):
                fight(unit_1, unit_2)

        # Returns True or False, according to living unit in army_1 or not.
        return not army_1.is_destroyed()

def fight(unit_1, unit_2):
    turn = 0
    while unit_1.is_alive and unit_2.is_alive:
        turn += 1

        attacking_unit = (unit_1, unit_2)[not turn%2]
        target_unit = (unit_1, unit_2)[turn%2]

        attacking_unit.hit([target_unit])

    # Returns True or False, according to unit_1 is still alive.
    return unit_1.is_alive




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
	ronald = Warlord()
	heimdall = Knight()

	assert fight(heimdall, ronald) == False

	my_army = Army()
	my_army.add_units(Warlord, 1)
	my_army.add_units(Warrior, 2)
	my_army.add_units(Lancer, 2)
	my_army.add_units(Healer, 2)

	enemy_army = Army()
	enemy_army.add_units(Warlord, 3)
	enemy_army.add_units(Vampire, 1)
	enemy_army.add_units(Healer, 2)
	enemy_army.add_units(Knight, 2)

	my_army.move_units()
	enemy_army.move_units()

	assert type(my_army.units[0]) == Lancer
	assert type(my_army.units[1]) == Healer
	assert type(my_army.units[-1]) == Warlord

	assert type(enemy_army.units[0]) == Vampire
	assert type(enemy_army.units[-1]) == Warlord
	assert type(enemy_army.units[-2]) == Knight

	#6, not 8, because only 1 Warlord per army could be
	assert len(enemy_army.units) == 6

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == True
    #print("Coding complete? Let's try tests!")

