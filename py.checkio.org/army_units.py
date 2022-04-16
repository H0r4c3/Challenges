'https://py.checkio.org/en/mission/army-units/'

'''
You are the developer of the new strategy game and you need to add the soldier creation process to it. 
Let's start with the 2 types - AsianArmy and EuropeanArmy (each of them will be a subclass of the Army - class with 
the methods for the creation of soldiers). Also there will be 3 types of soldiers in the game - Swordsman, Lancer, and Archer (also the classes). 
Each army has unique names for those 3 types. For the EuropeanArmy there are: Knight (for Swordsman), Raubritter (for Lancer), and Ranger (for Archer). 
For the AsianArmy: Samurai (for Swordsman), Ronin (for Lancer), and Shinobi (for Archer).
Each army can create all 3 types of the soldiers using the next methods:

train_swordsman (name) - create an instance of the Swordsman.
train_lancer (name) - create an instance of the Lancer.
train_archer (name) - create an instance of the Archer.

All 3 classes (Swordsman, Lancer, and Archer) should have the introduce() method, which returns the string that describes the soldiers in the following format:
"'type' 'name', 'army type' 'specialization(basic class)'", for example:
"Raubritter Harold, European lancer"
"Shinobi Kirigae, Asian archer"

In this mission you should use the Abstract Factory design pattern.
'''

class Soldier:
    def __init__(self, name, army, unique_name):
        self.name = name
        self.army = army
        self.unique_name = unique_name
        
    def introduce(self):
        return f'{self.unique_name} {self.name}, {self.army} {self.soldier_type}'

class Swordsman(Soldier):
    soldier_type = 'swordsman'
    
class Lancer(Soldier):
    soldier_type = 'lancer'
    
class Archer(Soldier):
    soldier_type = 'archer'

class Army:
    def train_swordsman(self, name):
        return Swordsman(name, self.continent, self.swordsman)
    
    def train_lancer(self, name):
        return Lancer(name, self.continent, self.lancer)
    
    def train_archer(self, name):
        return Archer(name, self.continent, self.archer)

class EuropeanArmy(Army):
    continent = 'European'
    swordsman = 'Knight'
    lancer = 'Raubritter'
    archer = 'Ranger'

class AsianArmy(Army):
    continent = 'Asian'
    swordsman = 'Samurai'
    lancer = 'Ronin'
    archer = 'Shinobi'



# Best Solution: 
# https://py.checkio.org/mission/army-units/publications/Phil15/python-3/short/?ordering=most_voted&filtering=all

class Soldier:
    def __init__(self, name, army, title):
        self.name, self.army, self.title = name, army, title
    def introduce(self):
        return f"{self.title} {self.name}, {self.army} {self.army_type}"

class Swordsman(Soldier):army_type = 'swordsman'
class Lancer(Soldier):army_type = 'lancer'
class Archer(Soldier):army_type = 'archer'

class Army:
    def train_swordsman(self, name):
        return Swordsman(name, self.nation, self.swordsman)
    def train_lancer(self, name):
        return Lancer(name, self.nation, self.lancer)
    def train_archer(self, name):
        return Archer(name, self.nation, self.archer)

class AsianArmy(Army):
    nation, swordsman, lancer, archer = 'Asian', 'Samurai', 'Ronin', 'Shinobi'
class EuropeanArmy(Army):
    nation, swordsman, lancer, archer = 'European', 'Knight', 'Raubritter', 'Ranger'



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"
    
    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")