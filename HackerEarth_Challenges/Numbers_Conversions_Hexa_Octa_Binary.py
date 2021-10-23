'https://www.geeksforgeeks.org/python-hex-function/'

# taking user input
print("Enter your choice: ", end='')
my_number = int(input())

# lstrip helps remove "0x" from the left 
# rstrip helps remove "L" from the right
# L represents a long number
hexa = hex(my_number).lstrip("0x").rstrip("L")
print(f'Hexadecimal form of {my_number} is {hexa}')
         
     
# Octal representation is done by removing the prefix "0o"
octa = oct(my_number).lstrip("0o").rstrip("L")
octa = oct(my_number)
print(f'Octal form of {my_number} is {octa}')
        
    
# Binary representation is done by the removing the "0b"
binary = bin(my_number).lstrip("0b").rstrip("L")
binary = bin(my_number)
print(f'Binary form of {my_number} is {binary}')