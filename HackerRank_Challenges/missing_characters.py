' Skill Certification Test nr. 1 - Python (Basics)'

'Missing Characters'

'''
Implement a function that takes a string that consists of lowercase letters and digits and returns a string
that consists of all digits and lowercase English letters that are not present in the string.
The digits should come first, in ascending order, followed by characters, also in ascending order

'''

def missingCharacters(s):
    digits = '01234567890'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    missing_digits = ''
    missing_letters = ''
    
    for item in digits:
        if item not in s:
            missing_digits += item
            
    for item in letters:
        if item not in s:
            missing_letters += item
            
    result = missing_digits + missing_letters
    
    return result

s = '7985interdisciplinary12'

result = missingCharacters(s)

print(result) 