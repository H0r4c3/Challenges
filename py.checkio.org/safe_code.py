'https://py.checkio.org/en/mission/safe-code/'

'''
Your task is to create a function that as input receives an equation in a form of a string with digits, 
erased places ('#') and one of the three arithmetic operations (+, - or *), for example - ##*##=302# 
As a result, your function should return a digit (from the interval 0-9), which when applied instead of all #, 
made the equation correct. Or -1 (minus one) if this isn’t possible.
Important note - none of the figures that already are in the equation can be in place of #. 
Also, if after the equal sign (=) there are 2 or more missing symbols, the answer cannot consist of zeros (00, 000, etc.).
'''

def safe_code(equation):
    for i in range(10):
        if str(i) in equation:
            continue
        elif (equation.startswith('#') or '=#' in equation) and i == 0:
            continue
        
        equation_new = equation.replace('#', str(i)).replace('=', '==')
        print(equation_new)
        print(eval(equation_new))
        
        if eval(equation_new):
            return i
        
    return -1



# Best Solution:
# https://py.checkio.org/mission/safe-code/publications/Moff/python-3/first/?ordering=most_voted&filtering=all

def safe_code_(equation):
    for i in range(10):
        if str(i) in equation or ((equation.startswith('#') or '=#' in equation) and i == 0):
            continue
        if eval(equation.replace('#', str(i)).replace('=', '==')):
            return i
    return -1



# Best Solution:
# https://py.checkio.org/mission/safe-code/publications/flpo/python-3/except-pass/?ordering=most_voted&filtering=all

from contextlib import suppress
from string import digits

def safe_code_(eq):
    def solve(i):
        try: return i not in eq and eval(eq.replace('#', i))
        except: pass
    eq = eq.replace('=', '==')
    return int(next(filter(solve, digits[eq.startswith('##') or '=##' in eq:]), -1))
    



if __name__ == '__main__':
    print("Example:")
    print(safe_code("-5#*-1=5#"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_code("-5#*-1=5#") == 0
    assert safe_code("##*##=302#") == 5
    assert safe_code("19--45=5#") == -1
    assert safe_code("##--11=11") == -1
    assert safe_code("#9+3=22") == 1
    assert safe_code("11*#=##") == 2
    assert safe_code("#9+3=12") == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")