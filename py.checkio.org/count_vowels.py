'https://py.checkio.org/en/mission/count-vowels/'

'''
This function should take a string as an input and return the count of vowels (a, e, i, o, u) in the string. 
The function should be case-insensitive.
'''

# 1. Using list comprehension
def count_vowels_(text: str) -> int:
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_list = [letter for letter in text if letter in VOWELS]
    return len(vowels_list)

# 2. Using regex
import re
def count_vowels(text: str) -> int:
    vowels_pattern = re.compile('[aeiou]', re.IGNORECASE)
    vowels_list = re.findall(vowels_pattern, text)
    return len(vowels_list)


print("Example:")
print(count_vowels("Hello"))

# These "asserts" are used for self-checking
assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")