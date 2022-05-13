'https://py.checkio.org/en/mission/dialogues/'

'''
Your task is to create a Chat class which could help a Human(name) and Robot(serial_number) to make a conversation. 
This class should have a few methods:
connect_human() - connects human to the chat.
connect_robot() - connects robot to the chat.
show_human_dialogue() - shows the dialog as the human sees it - as simple text.
show_robot_dialogue() - shows the dialog as the robot perceives it - as the set of ones and zeroes. 
To simplify the task, just replace every vowel ('aeiouAEIOU') with "0", and the rest symbols (consonants, white spaces and 
special signs like ",", "!", etc.) with "1".

Example :

chat = Chat()
karl = Human("Karl")
bot = Robot("R2D2")
chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi! What's new?")
bot.send("Hello, human. Could we speak later about it?")
chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""
'''

VOWELS = "aeiou"

class Chat:
    def __init__(self) -> None:
        self.human_dialogue = []
        self.robot_dialogue = []
    
    def connect_human(self, human):
        '''connects human to the chat'''
        human.chat = self
    
    def connect_robot(self, robot):
        '''connects robot to the chat'''
        robot.chat = self
    
    def show_human_dialogue(self):
        '''shows the dialog as the human sees it - as simple text'''
        print('\n'.join(self.human_dialogue))
        return '\n'.join(self.human_dialogue)
    
    def show_robot_dialogue(self):
        '''shows the dialog as the robot perceives it - as the set of ones and zeroes'''
        print('\n'.join(self.robot_dialogue))
        return '\n'.join(self.robot_dialogue) 


class Human:
    def __init__(self, name) -> None:
        self.name = name
        
    def send(self, message):
        robot_message = ''.join(['0' if char in VOWELS else '1' for char in message])
        self.chat.robot_dialogue.append(self.name + ' said: ' + robot_message)
        self.chat.human_dialogue.append(self.name + ' said: ' + message)


class Robot:
    def __init__(self, serial_number) -> None:
        self.serial_number = serial_number
        
    def send(self, message):
        robot_message = ''.join(['0' if char in VOWELS else '1' for char in message])
        self.chat.robot_dialogue.append(self.serial_number + ' said: ' + robot_message)
        self.chat.human_dialogue.append(self.serial_number + ' said: ' + message)
        
        
        
        
        

# Best Solution: 
# https://py.checkio.org/mission/dialogues/publications/kodix09/python-3/first/share/d3f24b1fdb78ccfb225c1357a9771883/

VOWELS = "aeiouAEIOU"

class Chat_:
    
    def __init__(self):
        self.human_dialogue = []
        self.robot_dialogue = []
    
    def connect_human(self, human):
        human.chat = self
        
    def connect_robot(self, robot):
        robot.chat = self
        
    def show_human_dialogue(self):
        print("\n".join(self.human_dialogue))
        return "\n".join(self.human_dialogue)
        
    def show_robot_dialogue(self):
        print("\n".join(self.robot_dialogue))
        return "\n".join(self.robot_dialogue)
        

class Human:
    
    def __init__(self, name):
        self.name = name
        
    def send(self, message):
        robot_message = "".join(["0" if char in VOWELS else "1" for char in message])
        self.chat.robot_dialogue.append(self.name + " said: " + robot_message)
        self.chat.human_dialogue.append(self.name + " said: " + message)

class Robot:
    
    def __init__(self, serial_number):
        self.serial_number = serial_number
        
    def send(self, message):
        self.chat.human_dialogue.append(self.serial_number + " said: " + message)
        robot_message = "".join(["0" if char in VOWELS else "1" for char in message])
        self.chat.robot_dialogue.append(self.serial_number + " said: " + robot_message)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")