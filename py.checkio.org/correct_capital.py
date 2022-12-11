'https://py.checkio.org/en/mission/correct-capital/'

'''
You are given a word in which letters can be in different cases. 
Your task is to check whether the case was used correctly in the line. 
If everything is correct - return True, if there are errors - return return False.

Examples of the correct use of cases:

All characters in the string are in uppercase. For example, "CHECKIO";
None of the characters are in uppercase. For example, "checkio";
Only the first character is in uppercase. For example, "Checkio".
'''

def correct_capital_(line: str) -> bool:
    return line.isupper() or line.islower() or (line[0].isupper and line[1:].islower())

def correct_capital(line: str) -> bool:
    return line.isupper() or line.islower() or line.istitle()


print("Example:")
print(correct_capital("Checkio"))

# These "asserts" are used for self-checking
assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")