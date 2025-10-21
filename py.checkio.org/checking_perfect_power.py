'https://py.checkio.org/en/mission/checking-perfect-power/share/a63a1cd1d46438c9761b201fa705f381/'

'''
A positive integer n is a perfect power if it can be expressed as the power be for some two integers b and e that are both greater than one.

This function should determine whether the positive integer n is a perfect power. 
'''

def perfect_power_(n):
    print(f'---n = {n}')
    e = 2
    while True:
        b = round(n ** (1 / e))
        print(f'b = {b}')
        if b == 1:  return False
        if n == b ** e: return True
        e += 1
        
def perfect_power_(n):
    print(f'---n = {n}')
    e = 2
    b = round(n ** (1 / e))
    
    while b > 1:
        print(f'e = {e}')
        
        b = round(n ** (1 / e))
        print(f'b = {b}')
        
        if n == b ** e: return True
        
        e += 1
        
    return False

e = 2
def perfect_power(n):
    print(f'---n = {n}')
    
    def base(n, e):
        print(f'e = {e}')
        b = round(n ** (1 / e))
        print(f'b = {b}')
        if b == 1:  return False
        
        if n == b ** e: 
            return True
        else:
            e += 1
            print(f'e after e += 1 = {e}')
            base(n, e)
            
    result = base(n, e)
    return result
    
        


# BEST Solution: 
# https://py.checkio.org/mission/checking-perfect-power/publications/ysenko/python-3/first-simple-exponent-search/?ordering=most_voted&filtering=all

import math 

def perfect_power_(n):
    if n <= 1:
        return False
    
    print(f'---n = {n}')
    print(f'int(math.log2(n)) = {int(math.log2(n))}')
    
    for e in range(2, int(math.log2(n)) + 1):
        b = round(n ** (1 / e))
        print(f'b = {b}')
        if b ** e == n:
            return True

    return False

# BEST 3rd Party Solution:
import sympy

def perfect_power_(n:int)-> bool:
    return bool(sympy.perfect_power(n))


# BEST Solution: https://py.checkio.org/mission/checking-perfect-power/publications/cerankas/python-3/first/?ordering=most_voted&filtering=all
def perfect_power_(n, p = 2):
    while True:
        b = round(n ** (1 / p))
        print(f'b = {b}')
        if b == 1:  return False
        if n == b ** p: return True
        p += 1




print("Example:")
#print(perfect_power(9))

# These "asserts" are used for self-checking
assert perfect_power(8) == True
assert perfect_power(42) == False
assert perfect_power(441) == True
assert perfect_power(469097433) == True
#assert perfect_power(4922235242952026704037113243122008064) == True
#assert perfect_power(4922235242952026704037113243122008063) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")