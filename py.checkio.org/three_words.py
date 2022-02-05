'https://py.checkio.org/en/mission/three-words/'

'''
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. 
You should check if the string contains three words in succession . 
For example, the string "start 5 one two three 7 end" contains three words in succession.
'''

def checkio(words: str) -> bool:
    my_list = words.split()
    counter = 0
    for item in my_list:
        if item.isalpha():
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0
    
    return False


# Clear solution: https://py.checkio.org/mission/three-words/publications/knezi/python-3/regexp/?ordering=most_voted&filtering=choice
import re
def checkio(words):
    return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))



# Best solution: https://py.checkio.org/en/mission/three-words/
import re

def checkio(words):
    return True if re.search('\D+\s\D+\s\D+', words) else False




#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"