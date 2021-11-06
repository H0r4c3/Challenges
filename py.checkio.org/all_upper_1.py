'https://py.checkio.org/en/mission/all-upper/'

'''
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.

Output: a boolean.
'''

def is_all_upper(text: str) -> bool:
    if text == '':
        return True
    for item in text:
        if item.isupper() or item == ' ' or item in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            continue
        else:
            return False
    return True

text = 'all lower'

if __name__ == '__main__':

    print(is_all_upper(text))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True