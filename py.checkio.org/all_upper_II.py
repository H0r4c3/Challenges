'https://py.checkio.org/en/mission/all-upper-ii/'

'''
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.

Input: A string.

Output: a boolean.
'''

import re

def is_all_upper(text: str) -> bool:
    if text == '':
        return False
    
    #regex = re.compile('\w+[^\d]')
    regex = re.compile('[a-zA-Z]')
    print(re.findall(regex, text))
    if re.findall(regex, text) == []:
        return False    
    
    for item in text:
        if item.islower():
            return False
    
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    assert is_all_upper("Hi") == False
    assert is_all_upper("   ") == False
    assert is_all_upper("123") == False