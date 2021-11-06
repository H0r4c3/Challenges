'https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python'

'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 

You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

def count_bits(n):
    counter = 0
    binary = bin(n)
    binary = str(binary)
    for item in binary:
        if item == '1':
            counter += 1
            
    return counter

n = 1234 # -> 10011010010 -> result = 5
result = count_bits(n)
print(result)