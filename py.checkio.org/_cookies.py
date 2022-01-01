'https://py.checkio.org/en/mission/cookies/'

'''
This is pretty much a technical mission.

You have raw HTTP cookies . Your mission is to extract the value of a specific cookie by its name.

Input: Two arguments. Both are strings. The first one is the string of raw cookies, and the second one is the name of the cookie we are looking for.

Output: A string. Extracted value.
'''

import re
def get_cookie(cookie, name):
    pattern = re.compile(name + '=([\w]+)' )
    return pattern.search(cookie).group(1)


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light', 'theme=light'
    assert get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
    print("Looks like you know everything. It is time for 'Check'!")