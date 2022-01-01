'https://py.checkio.org/en/mission/caps-lock/'

'''
Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the key “a” by itself. 
(When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure the accents, 
he is more careful in the presence of such raffinated characters ([Shift] + [Char]) and will press the keys correctly.) 
Compute and return the result of having Joe type in the given text. The “Caps Lock” key affects only the letter keys from “a” to “z” , and 
has no effect on the other keys or characters. “Caps Lock” key is assumed to be initially off.

For Joe's keyboard, Caps Lock is always uppercase a letter. That means if Caps Lock is on, and Joe does Shift + b - he gets 'B' (in upper case) printed.

Input: A string. The typed text.

Output: A string. The showed text after being typed.
'''
import re

def caps_lock(text: str) -> str:
    #indexes = list()
    #indexes_for_a = re.finditer('[aA]+', text)
    start = ''
    if text.startswith('A'):
        start = 'A'
        text = text.replace('A', '')
    
    text_without_a = re.split('[aA]+', text)
    print(text_without_a)
    
    # for match in indexes_for_a:
    #     indexes.append(match.span())
        
    # indexes = [item[0] for item in indexes]
    
    result = [item.upper() if text_without_a.index(item) % 2 != 0 else item for item in text_without_a]
    
    print(result)
            
    return start + ''.join(result)


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))
    print(caps_lock("Always wanted to visit Zambia."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")