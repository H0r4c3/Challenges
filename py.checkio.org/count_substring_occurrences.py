'https://py.checkio.org/en/mission/count-substring-occurrences/'

'''
This function should take a main string and a substring as inputs and return the number of occurrences of the substring within the main string. 
It should not be case-sensitive and may overlap.
'''

import re

def count_occurrences(main_str: str, sub_str: str) -> int:
    print('------------------')
    print(main_str)
    print(sub_str)
    print('------------------')
    
    matches = re.finditer(f'(?=({sub_str.lower()}))', main_str.lower())
    result = [match.group(1) for match in matches]
    print(result)
    
    return len(result)


# Best Solution: 
# https://py.checkio.org/mission/count-substring-occurrences/publications/freeman_lex/python-3/second/?ordering=most_voted&filtering=all

import re

def count_occurrences_(main_str: str, sub_str: str) -> int:
    
    matches = re.findall(fr'(?={sub_str})', main_str, flags=re.IGNORECASE)
    
    return len(matches)



print("Example:")
#print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")