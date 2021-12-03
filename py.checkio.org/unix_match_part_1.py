'https://py.checkio.org/en/mission/unix-match-part-1/'

'''
Let me show you what I mean by matching the filenames in the unix-shell. For example, * matches everything and *.txt matches all of the files that have txt extension. 
Here is a small table that shows symbols that can be used in patterns

*	matches everything
?	matches any single character

Input: Two arguments. Both are strings.

Output: Bool.
'''

import re

def unix_match(filename: str, pattern: str) -> bool:
    
    pattern1 = pattern.replace('.', '\.')
    pattern2 = pattern1.replace('*', '.+')
    pattern3 = pattern2.replace('?', '.')
    print(f'pattern3 = {pattern3}')
    
    regex = re.compile(pattern3)
    
    result = re.search(regex, filename)
    print(result)
    
    if result == None:
        return False
    else:
        return True


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    print(unix_match("name....","name.*"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    assert unix_match("name....","name.*") == True