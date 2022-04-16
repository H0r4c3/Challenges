'https://py.checkio.org/en/mission/restricted-prime/'

'''
Given a number (0 < n < 10000), you should check if it is a prime or not. 
Your solution should not contain any of the forbidden words, symbols or digits (even as a part of another word).

The list of forbidden words and symbols:

import
div
eval
range
len
⁄ % −
digits (0-9)
'''

# Solution using regex (NOK)
# https://iluxonchik.github.io/regular-expression-check-if-number-is-prime/

import re

def checkio_(number):
    def is_prime(number):
        return re.compile(r'^1?$|^(11+)\1+$').match('1' * number) is None
    
 
    
# Another Solution (NOK)
import sympy

def checkio(number):
    return sympy.isprime(number)




# Best Solution
# https://py.checkio.org/mission/restricted-prime/publications/_Chico_/python-3/first/share/28b6fbd02a5f374c99d90c8fa8480612/

checkio_ = lambda n: all(i==n or pow(i, n+~False, n)==True for i in map('   , . "'.index,',."'))


# Another Best Solution:
# https://py.checkio.org/mission/restricted-prime/publications/bravebug/python-3/first/?ordering=most_voted&filtering=all

def checkio(number):
    counter = True + True
    while counter < number:
        if not pow(number, True, counter):
            return False
        counter += True
    return True






if __name__ == "__main__":
    assert checkio(13) == True
    assert checkio(15) == False
    assert checkio(17) == True
    print('Done!!!')