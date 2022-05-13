'https://py.checkio.org/en/mission/multicolored-lamp/'

'''
The New Year is coming and you've decided to decorate your home. 
But simple lights and Christmas decorations are so boring, so you have figured that you can use your programing 
skills and create something really cool and original. 
Your task is to create the class Lamp() and method light() which will make the lamp glow with one of the four colors 
in the sequence - (‘Green’, ‘Red’, ‘Blue’, ‘Yellow’). When the light() method is used for the first time, the color 
should be 'Green', the second time - 'Red' and so on. If the current color is 'Yellow', the next color should be 'Green' and so on.
'''

class Lamp:
    pass



# Best Solution: 
# https://py.checkio.org/mission/multicolored-lamp/publications/sawako.oono/python-3/first/share/a37b952bbaa169d348568c0ab939f07a/

class Lamp:
    def __init__(self):
        self.colors = ["Green","Red","Blue","Yellow"]
        self.pos = 0
    
    def light(self):
        if self.pos == 4:
            self.pos = 1
        else:
            self.pos += 1
        self.color = self.colors[self.pos-1]
        return self.color



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light() #Green
    lamp_1.light() #Red
    lamp_2.light() #Green
    
    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")