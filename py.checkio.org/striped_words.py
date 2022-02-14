'https://py.checkio.org/en/mission/striped-words/'

'''
You are given a block of text with different words. 
These words are separated by whitespaces and punctuation marks. 
Numbers are not considered as words in this mission (a mix of letters and digits is not a word either). 
You should count the number of words (striped words) where the vowels with consonants are alternating; 
words that you count cannot have two consecutive vowels or consonants. 
The words consisting of a single letter are not striped -- don't count those. Casing is not significant for this mission.
'''

import re

def checkio(line: str) -> str:
    VOWELS = 'aeiouyAEIOUY'
    CONSONANTS = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    result = list()
    print(line)
    
    # split the string in words
    pattern = re.compile('\W+')
    
    words = re.split(pattern, line)
    words = [item for item in words if len(item)>1]
    print(words)
    
    for word in words:                      
        if word[0] in VOWELS:
            if (all(char in VOWELS for char in word[0:len(word):2]) and all(char in CONSONANTS for char in word[1:len(word):2])): 
                result.append(word)
            
        elif word[0] in CONSONANTS:
            if (all(char in CONSONANTS for char in word[0:len(word):2]) and all(char in VOWELS for char in word[1:len(word):2])):
                result.append(word)
            
    print(result)
    return len(result)


if __name__ == '__main__':
    print("Example:")
    #print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    assert checkio("For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words.") == 6
    assert checkio("1st 2a ab3er root rate") == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")