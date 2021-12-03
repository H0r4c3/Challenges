'https://py.checkio.org/en/mission/unix-match/'

'''
You need to find out if the given unix pattern matches the given filename.

For example, * matches everything and *.txt matches all of the files that have txt extension. Here is a small table that shows symbols that can be used in patterns.

*	matches everything
?	matches any single character
[seq]	matches any character in seq
[!seq]	matches any character not in seq

Input: Two arguments. Both are strings.

Output: Bool.
'''

import re

def unix_match(filename: str, pattern: str) -> bool:

    list = [('.', '\.'), ('?', '.'), ('[.]', '.'), ('[[]', '\['), ('[]]', '\]')]
    
    x = pattern
    
    for a, b in list:
        x = x.replace(a, b)
        
    if '[!]' not in pattern:
        x = x.replace('[!', '[^')
    else:
        x = x.replace('[!]', '\[!\]')
        
    if '[*]' not in pattern:
        x = x.replace('*', '.+')

    try:
        return re.match(x, filename) != None
    except:
        return pattern == filename


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    assert unix_match("1name.txt","[!1234567890]*") == False
    