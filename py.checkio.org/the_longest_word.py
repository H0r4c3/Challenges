'https://py.checkio.org/en/mission/the-longest-word/'

'''
This function should take a string without punctuation marks as an input and return the longest word in the string. 
If there are multiple words of the same length, return the first one that appears.
'''
# 1. Solution

def longest_word_(sentence: str) -> str:
    sentence_list = sentence.split()
    if sentence_list:
        max = sentence_list[0]
    else:
        return ''
    
    for item in sentence_list:
        print(max)
        if len(item) > len(max):
            max = item
            
    print(max)
    return max



# 2. Solution using regex

import re

def longest_word_(sentence):
    words = re.findall(r'\w+', sentence)

    if not words:
        return ''
    
    longest = max(words, key=len)
    return longest

# 3. BEST Solution:

def longest_word(sentence: str) -> str:
    
    return max(sentence.split(),default='', key=len)


print("Example:")
#print(longest_word("hello world"))

# These "asserts" are used for self-checking
assert longest_word("hello world") == "hello"
assert longest_word("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"
assert longest_word("jumped over the lazy dog") == "jumped"
assert longest_word("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word("") == ""
assert longest_word(" ") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
