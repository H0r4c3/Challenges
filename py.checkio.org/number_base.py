'https://py.checkio.org/en/mission/number-radix/'

'''
You are given a positive number as a string along with the radix for it. 
Your function should convert it into decimal form. The radix is less than 37 and greater than 1. 
The task uses digits and the letters A-Z for the strings.

Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.
'''

def checkio(str_number: str, radix: int) -> int:
    try:
        return int(str_number, radix)
    except ValueError:
        return -1




if __name__ == '__main__':
    print('Example:')
    print(checkio("AF", 16))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")