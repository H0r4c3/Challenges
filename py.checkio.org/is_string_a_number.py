'https://py.checkio.org/en/mission/is-string-a-number/share/5d8662578a85730ed0d6b9bd732fb725/'

'''
You are given a string. 
Your function should return True if the string is a valid number (contains digits only), otherwise - False.
'''

def is_number(val: str) -> bool:
    try:
        int(val)
        return True
    except:
        return False


print("Example:")
print(is_number("34"))

# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("a5") == False
assert is_number("ITS A NUMBER") == False
assert is_number("5a") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")