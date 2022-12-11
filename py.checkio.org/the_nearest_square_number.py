'https://py.checkio.org/en/mission/the-nearest-square-number/'

'''
You have some number and you are trying to find the nearest square number (a perfect square). 
For example, if we start with the number 8, then the two nearby square numbers are 4 (sqrt(4) == 2) and 9 (sqrt(9) == 3). 
So the answer is 9, because 9 is the nearest.
'''
import math

def nearest_square(number):
    nextN = math.floor(math.sqrt(number)) + 1
    prevN = math.ceil(math.sqrt(number)) - 1
    
    n = nextN * nextN - number
    p = number - prevN * prevN 
    
    print(nextN * nextN)
    print(prevN * prevN)
    return nextN * nextN if n < p else prevN * prevN


# Best Solution: 
# https://py.checkio.org/mission/the-nearest-square-number/publications/przemyslaw.daniel/python-3/1-liner-round/?ordering=most_voted&filtering=all

def nearest_square(number):
    return round(number**0.5)**2


# Best Solution:
# https://py.checkio.org/mission/the-nearest-square-number/publications/kdim/python-3/1-line-clear-math/#comment-116070

from math import sqrt
def nearest_square(number):
    return round(sqrt(number)) ** 2


if __name__ == '__main__':
    print("Example:")
    print(nearest_square(8))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert nearest_square(8) == 9
    assert nearest_square(13) == 16
    assert nearest_square(24) == 25
    assert nearest_square(9876) == 9801
    print("Coding complete? Click 'Check' to earn cool rewards!")