'https://py.checkio.org/en/mission/long-repeat/'

'''
This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. 
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". 
The last substring is the longest one, which makes it the answer.
'''

import re

def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    pattern = re.compile(r'(.)\1*')
    result_iterator = pattern.finditer(line)
    result = [match.group() for match in result_iterator]
    result.sort(key=len)
    
    return len(result[-1]) if result != [] else 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')