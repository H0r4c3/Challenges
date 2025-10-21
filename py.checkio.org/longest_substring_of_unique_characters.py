'https://py.checkio.org/en/mission/longest-substring-of-unique-characters/'

'''
Given a string, find the length of the longest substring without repeating characters.
'''

import logging

log_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\py.checkio.org\longest_substring_of_unique_characters.log'
  
#Create and configure logger
#logging.basicConfig(filename=path, format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=log_path, 
                    filemode='w')

logger = logging.getLogger('main')

def longest_substr(s: str) -> int:
    logging.info(f'START using string = {s}')
    length, result = 1, 1
    if s:
        etalon = s[0]
    else:
        return 0
    
    for i in range(1, len(s)):
        logging.debug(f'etalon = {etalon}')
        if s[i] not in etalon:
            length += 1
            logging.debug(f'length = {length}')
            if length > result: 
                result = length
            etalon += s[i]
        else:
            pos = etalon.index(s[i])
            logging.debug(f'pos of repeated char {s[i]} = {pos}')
            etalon = etalon[pos+1:] + s[i]
            logging.debug(f'new etalon = {etalon}')
            length = len(etalon)
    
    print(result)    
    logging.info(f'result = {result}')
    return result


# Best Solution: https://py.checkio.org/mission/longest-substring-of-unique-characters/publications/Olpag/python-3/maxlength-lensubstr/?ordering=most_voted&filtering=all

def longest_substr(s: str) -> int:
    substr, length = '', 0
    for char in s:
        if char not in substr:
            substr += char
            length = max(length, len(substr))
        else:
            start = substr.index(char) + 1
            substr = substr[start:] + char
    return length


print("Example:")
#print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcdef") == 6
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")