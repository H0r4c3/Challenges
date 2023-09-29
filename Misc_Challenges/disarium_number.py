'''
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
'''

def is_disarium(number):
    # Convert the number to a string to access individual digits
    num_str = str(number)
    
    # Calculate the sum of digits raised to their respective positions
    digit_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    
    # Check if the sum is equal to the original number
    return digit_sum == number

assert is_disarium(89) == True
assert is_disarium(135) == True
assert is_disarium(10) == False
assert is_disarium(23) == False

print('Done!!!')