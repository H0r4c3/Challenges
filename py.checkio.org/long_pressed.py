'https://py.checkio.org/en/mission/long-pressed/'

'''
Return True if the printed message matches the original one, taking into account possible long keystrokes. 
Or False if there are errors or no long-pressed letters.
'''
from itertools import groupby
from collections import Counter

def remove_consecutive_duplicates(s):
    my_list = [i for i, _ in groupby(s)]
    my_string = ''.join(my_list)
    return my_string


def compare_strings(string1, string2):
    # find the counter for every letter in both strings
    char_counts1 = Counter(string1)
    char_counts2 = Counter(string2)
    
    count_dict1 = dict(char_counts1.items())
    count_dict2 = dict(char_counts2.items())
    print(f'1. {count_dict1} \n')
    print(f'2. {count_dict2} \n')
    
    for item in count_dict1.keys():
        try:
            if count_dict2[item] < count_dict1[item]:
                return False
        except:
            return False
    
    return True


def long_pressed(text: str, typed: str) -> bool:
    if text == typed:
        return False
    
    if compare_strings(text, typed) == False:
        return False
    
    print(remove_consecutive_duplicates(text))
    print(remove_consecutive_duplicates(typed))
    
    return remove_consecutive_duplicates(text) == remove_consecutive_duplicates(typed)


# Best Solution: https://py.checkio.org/mission/long-pressed/publications/Wartem/python-3/second-clear-and-simple-lstrip-instead-of-regex/?ordering=most_voted&filtering=all

def long_pressed_(text: str, typed: str) -> bool:
    text, typed = text.lower(), typed.lower()
    
    if text == typed:
        return False
    
    while(text):
        typed = typed.lstrip(text[0])
        text = text[1:]

    return not typed
    

# Best Solution: https://py.checkio.org/mission/long-pressed/publications/mu_py/python-3/refullmatch/?ordering=most_voted&filtering=all

from re import fullmatch, escape

def long_pressed_(text: str, typed: str) -> bool:
    if text == typed: return False                 # I don't like this precondition ;-)

    pattern = '+'.join(escape(c) for c in text)
    return bool(fullmatch(pattern, typed))

# there are several matching-procedures in re:
# match()        search pattern from the beginning of string only
# search()       search pattern anywhere in the string
# fullmatch()    check, that the pattern matches the whole string
# see https://docs.python.org/3/library/re.html#search-vs-match



print("Example:")
#print(long_pressed("alex", "aaleex"))

# These "asserts" are used for self-checking
assert long_pressed("alex", "aaleex") == True
assert long_pressed("welcome to checkio", "weeeelcome to cccheckio") == True
assert long_pressed("there is an error here", "there is an errorrr hereaa") == False
assert long_pressed("hi, my name is...", "hi, my name is...") == False
assert long_pressed('welcome boss!', 'welcooome bos!!') == False
assert long_pressed('hello from usaaaa', 'hello from japannnn') == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
