'https://py.checkio.org/en/mission/acceptable-password-iv/'

'''
In this mission you need to create a password verification function.

Those are the verification conditions:

- the length should be bigger than 6;
- should contain at least one digit, but it cannot consist of just digits;
- if the password is longer than 9 - previous rule (about one digit), is not required.
'''

import re

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6 and (re.findall('[\D]+[\d]+', password) or len(password) > 9):
        return True
    else:
        return False

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")