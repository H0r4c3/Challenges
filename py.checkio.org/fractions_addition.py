'https://py.checkio.org/en/mission/fractions-addition/'

'''
Your task is to write a function which takes the tuple of tuples containing fractions as an argument and returns the sum of those fractions. 
The fractions will look like this: (x, y), where 'x' is the numerator, and 'y' is the denominator. For example, (2, 3) means 2/3. 
If the numerator is greater than the denominator (after the addition) you should extract the integer part and put it before the fraction.
'''
from math import gcd, lcm

def add_fractions_(fracts):
    print(fracts)
    
    denominators = [item[1] for item in fracts]
    print(denominators)
    
    least_common_multiple = lcm(*denominators)
    print(least_common_multiple)
    
    numerators = [item[0] for item in fracts]
    print(numerators)
    
    sum_numerators = sum([fraction[0] * least_common_multiple//fraction[1] for fraction in fracts])
    print(sum_numerators)
    
    result = (sum_numerators, least_common_multiple)
    greatest_common_divisor = gcd(result[0], result[1])
    result = (result[0]//greatest_common_divisor, result[1]//greatest_common_divisor)
    print(f'result = {result}')
    
    
    if result[0] > result[1]:
        if result[0] % result[1] == 0:
            return result[0] // result[1]
        c = result[0] // result[1]
        r = result[0] % result[1]
        print(f'{c} and {r}/{result[1]}')
        return f'{c} and {r}/{result[1]}'
    elif result[0] < result[1]:
        print(f'{result[0]}/{result[1]}')
        return f'{result[0]}/{result[1]}'
    else:
        print(result[0] // result[1])
        return result[0] // result[1]
    

# Best Solution:
# https://py.checkio.org/mission/fractions-addition/publications/kurosawa4434/python-3/fractionsfraction/?ordering=most_voted&filtering=all

from fractions import Fraction


def add_fractions(fracts):

    #total = sum(Fraction(*f) for f in fracts)
    total = sum(Fraction(*f) for f in fracts)
    print(f'total = {total}')
    whole = total.numerator // total.denominator
    rest = total - whole

    if whole and rest:
        return f'{whole} and {rest}'
    elif whole:
        return whole
    else:
        return f'{rest}'
    
    

# Another Best Solution:
# https://py.checkio.org/mission/fractions-addition/publications/veky/python-3/count-the-fs-an-exercise-in-perception/?ordering=most_voted&filtering=all

from fractions import Fraction
from itertools import starmap

def add_fractions(fracts):
    result = floor, rest = divmod(sum(starmap(Fraction, fracts)), 1)
    return ' and '.join(map(str, filter(None, result))) if rest else floor

  

if __name__ == '__main__':
    print("Example:")
    print(add_fractions(((2, 3), (2, 3))))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert add_fractions(((2, 3), (2, 3))) == "1 and 1/3"
    assert add_fractions(((1, 3), (1, 3))) == "2/3"
    assert add_fractions(((1, 3), (1, 3), (1, 3))) == 1
    assert add_fractions(((1, 2), (1, 4), (1, 4), (1, 3))) == "1 and 1/3"
    assert add_fractions(([2,1],[3,1],[4,2],[5,1])) == 12
    print("Coding complete? Click 'Check' to earn cool rewards!")