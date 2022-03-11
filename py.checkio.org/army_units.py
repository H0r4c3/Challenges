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

class Army:
    pass

class Swordsman:
    pass

class Lancer:
    pass

class Archer:
    pass

class AsianArmy(Army):
    pass

class EuropeanArmy(Army):
    pass



# Best Solution: 
# https://py.checkio.org/mission/army-units/publications/kurosawa4434/python-3/first/share/cc6fb88b6b50e6bbf558cc706c3561ad/

class job:
    def __init__(self, job_name, area, name):
        self.job_name = job_name
        self.name = name
        self.area = area

    def introduce(self):
        pass


class Swordsman(job):
    def introduce(self):
        return f'{self.job_name} {self.name}, {self.area} swordsman'


class Lancer(job):
    def introduce(self):
        return f'{self.job_name} {self.name}, {self.area} lancer'


class Archer(job):
    def introduce(self):
        return f'{self.job_name} {self.name}, {self.area} archer'


class Army:
    def train_swordsman(self, name):
        pass

    def train_lancer(self, name):
        pass

    def train_archer(self, name):
        pass


class AsianArmy(Army):
    def __init__(self):
        self.area = 'Asian'

    def train_swordsman(self, name):
        return Swordsman('Samurai', self.area, name)

    def train_lancer(self, name):
        return Lancer('Ronin', self.area, name)

    def train_archer(self, name):
        return Archer('Shinobi', self.area, name)


class EuropeanArmy(Army):
    def __init__(self):
        self.area = 'European'

    def train_swordsman(self, name):
        return Swordsman('Knight', self.area, name)

    def train_lancer(self, name):
        return Lancer('Raubritter', self.area, name)

    def train_archer(self, name):
        return Archer('Ranger', self.area, name)



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