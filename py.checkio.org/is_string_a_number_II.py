'https://py.checkio.org/en/mission/is-string-a-number-part-ii/share/f8af69aa79141ec92a4ebdb62f39579e/'

'''
You are given a string. Your function should return True if the string is a valid number (contains only digits and "+-." at proper places), otherwise - False. 
Look at the mask:

[+- ][zero or more digits][.][zero or more digits]

Of course, not all parts are necessary (but at least one digit part is!). 
For example, "+10." or "-.55" are valid numbers, where part equal 0 is omitted.
'''
import re

def is_number(val: str) -> bool:
    print(f'val = {val}')
    
    result = re.search(r'^[+-]?(\d+\.\d*|\d*\.\d+|\d+)$', val)
    print(result)
    return bool(result)


# Best Solution:
# https://py.checkio.org/mission/is-string-a-number-part-ii/publications/review/clear/

def is_number_(val: str) -> bool:
    try:
        float(val)
        return True
    except:
        return False
    

# Best Solution:
# https://py.checkio.org/mission/is-string-a-number-part-ii/publications/Kolia951/python-3/regex-will-kill-me/?ordering=most_voted&filtering=all

def is_number_(val: str) -> bool:
    regex = r"^[+-]?(\d+\.{1}\d*|\d*\.{1}\d+|\d+)$"
    result = re.search(regex, val)
    
    return bool(result)



print("Example:")
#print(is_number("10"))

# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("+10.0") == True
assert is_number("1OOO") == False
assert is_number("1.") == True
assert is_number("+.l") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")