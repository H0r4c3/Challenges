'https://py.checkio.org/en/mission/count-and-say/'

'''
Given a string of digits that is guaranteed to contain only digit characters from 0123456789, 
read that string “out loud” by saying how many times each digit occurs consecutively in the current bunch of digits, 
and then return the string of digits that you just said out loud.
'''

# My Solution:

def count_and_say_(digits: str) -> str:
    if digits == '':
        return ''
    
    result = list()
    repetitions = [digits[0]]
    
    for i in range(1, (len(digits))):
        if digits[i] == digits[i-1]:
            repetitions.append(digits[i])
        else:
            result.append(str(len(repetitions)))
            result.append(repetitions[0])
            repetitions = [digits[i]]
    
    # for the last digit        
    result.append(str(len(repetitions)))
    result.append(repetitions[0])
    
    result = ''.join(result) 
    print(result)    
    return result


# Solution using regex
'''
(.) captures any character
\1 is a backreference to the first captured group (.)
* matches zero or more occurrences of the character captured by (.)
'''

import re

def count_and_say(digits: str) -> str:
    result = ''
    
    pattern = r'(.)\1*'
    digits_found = re.finditer(pattern, digits)
   
    for groups in digits_found:
        print(groups.group())
        print(len(groups.group()))
        print(groups.group()[0])
        result += str(len(groups.group())) + groups.group()[0]
    
    print(result)
        
    return result


# Another Solution (using groupby) 
# https://py.checkio.org/mission/count-and-say/publications/Kolia951/python-3/groupby-it/?ordering=most_voted&filtering=all

from itertools import groupby

def count_and_say(digits: str) -> str:
    final_string = ''
    
    for digit, how_many in groupby(digits):
        pair = str(len(list(how_many))) + digit
        final_string += pair

    return final_string


#print("Example:")
#print(count_and_say("123"))

# These "asserts" are used for self-checking
#assert count_and_say('111100000002222222333444555') == ''
assert count_and_say("123") == "111213"
assert count_and_say("333388822211177") == "4338323127"
assert count_and_say("1") == "11"
assert count_and_say("") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")