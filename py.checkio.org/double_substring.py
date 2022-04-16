'https://py.checkio.org/en/mission/double-substring/'

'''
This is the third mission of the series, and it’s the only one where you have to return not a substring but a substring length. 
You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps. 
For example, in a string "abcab" the longest substring that repeats more than once is "ab", so the answer should be 2 (length of "ab")
'''
import re

def double_substring_(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    pattern = re.compile(r'(.+)(?=.*\1)')
    list_of_subs = pattern.findall(line)
    print(list_of_subs)
    if not list_of_subs:
        return 0
    
    longest_sub = max(list_of_subs, key=lambda m: len(m))
    print(longest_sub)

    return len(max(list_of_subs, key=lambda m: len(m)))

'''
EXPLANATIONS for (?=(.*).*\1)
. - any symbol except '\n'
* - 0 or more repetitions of the previous symbol
.* - several symbols
(.*) - brackets are a capturing group. It is used to catch and “memorize” what we matched inside the brackets (a repeating substring we are looking for)
next .* means that there might be any number (including 0) of symbols between the repetitions
\1 means the same string we found in the first capturing group (our substring).
(?=pattern) - is a positive lookahead. It matches if pattern matches next, but doesn’t consume any of the string. 
In terms of our task it helps us to find all the repeating substrings. 
If we typed just '(.*).*\1' (without the lookaround), we would find only the first repeating substring, 
because it would consume some parts of the string and wouldn’t be able to find the other repeating substrings.

'''


# Best Solution
# https://py.checkio.org/mission/double-substring/publications/colinmcnicholl/python-3/first/share/0524f3eecb2980ffa00c2d60312f5c8e/

import re

def double_substring_(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    matches = re.findall(r'(.+)(?=.*\1)', line)
    print(matches)
    
    largest = '' if not matches else max(matches, key=lambda m: len(m))
    print(largest)
    
    return len(largest)


# Another great solution: 
# https://py.checkio.org/mission/double-substring/publications/przemyslaw.daniel/python-3/7-liner-simple/?ordering=most_voted&filtering=all

def double_substring(string):
    result = 0 
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string.count(string[i:j]) > 1:
                result = max(result, j-i)
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')