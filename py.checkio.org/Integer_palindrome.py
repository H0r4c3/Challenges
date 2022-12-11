'https://py.checkio.org/en/mission/integer-palindrome/'

'''
You need to determine whether the given integer is a palindrome or not in base B.
'''

# convert a decimal number to another base
def dec_to_base(number, base):
    num = []                            # Initialize and empty list for the converted number
    while number:                       # Loop: To convert the number to base B, it must be divided by the base until it is 0.
        number, rem = divmod(number, base) # ... Divide number by base ...
        num.insert(0, rem)
    return num


# convert a decimal number to another base
# def dec_to_base_(num, base):  #Maximum base - 36
#     base_num = ""
#     while num>0:
#         dig = int(num % base)
#         if dig<10:
#             base_num += str(dig)
#         else:
#             base_num += chr(ord('A') + dig-10)  #Using uppercase letters
#         num //= base
#     base_num = base_num[::-1]  #To reverse the string
#     return base_num


def int_palindrome(number: int, B: int) -> bool:
    base_num = dec_to_base(number, B)
    print(base_num)
    
    return base_num == base_num[::-1]


print("Example:")
#print(int_palindrome(455, 2))

assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")