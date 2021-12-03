'https://py.checkio.org/en/mission/acceptable-password-iii/'

'''
In this mission you need to create a password verification function.

Those are the verification conditions:

- the length should be bigger than 6;
- should contain at least one digit, but cannot consist of just digits.

Input: A string.

Output: A bool.
'''

import re

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6 and re.findall('[\D]+[\d]+', password):
        return True
    else:
        return False

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False