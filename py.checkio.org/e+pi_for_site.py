'https://py.checkio.org/en/mission/epi/'

'''
In this challenge, you will be given a result, and your task is to find the arithmetic expression 
using only the numbers pi and e that yields that result. 
You can use addition, subtraction, multiplication, division, and exponentiation, 
and each number (pi and e) can appear at most two times (parenthesis are excluded). 
If there are multiple solutions, return the one that comes first alphabetically (no spaces). 
The calculated result must be equal with an error smaller than 1 x 10-10.
'''

"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

from math import e, pi, isclose
from itertools import combinations, combinations_with_replacement, permutations


def find_arithmetic_expression():
    '''
    Brute-force: generate all possible arithmetic expressions using e and pi
    '''
    operators_comb_all = list()
    expressions = list()
    operands = ['e', 'pi']
    operators = ['+', '-', '*', '/', '**']
    
    # all combinations from operands list
    operands_all = [('e', 'e'), ('pi', 'pi'), ('e', 'pi'), ('pi', 'e'), 
                 ('e', 'e', 'pi'), ('pi', 'pi', 'e'), ('e', 'pi', 'pi'), ('pi', 'e', 'e'), 
                 ('e', 'e', 'pi', 'pi'), ('pi', 'pi', 'e', 'e'), ('e', 'pi', 'e', 'pi'), ('pi', 'e', 'pi', 'e')]
    
    # all combinations from operators list
    for rep in range(1, 4):
        operators_comb = list(combinations_with_replacement(operators, rep))
        for item in operators_comb:
            perm_item = set(permutations(item, rep))
            operators_comb_all.extend(perm_item)
    
    # combine operands with operators
    for operands in operands_all:
        for operators in operators_comb_all:
            if len(operands) == len(operators) + 1:
                expression = intercalation(operands, operators)
                expressions.append(expression)
    expressions.insert(0, 'e')
    expressions.insert(0, 'pi')
           
    return expressions


def intercalation(operands, operators):
    '''
    Create a new list whose even-index values come from the first list and whose odd-index values come from the second list
    '''
    expression = [x for y in zip(operands, operators) for x in y] + [operands[-1]]
    # convert to string
    expression = ''.join(expression)
    
    return expression


def verification(expressions, result):
    '''
    Evaluate each expression and check if it matches the result
    '''
    for expression in expressions:
        try:
            value = eval(expression)
            if isclose(value, result, rel_tol=1e-10):
                return expression
        except ZeroDivisionError as e:
            print('A ZeroDivisionError occurred:', e)
        except OverflowError as e:
            print('OverflowError occurred:', e)

    return None
    

def checkio(n: float) -> str:
    expressions = find_arithmetic_expression()
    
    answer = verification(expressions, n)
    print(f'answer = {answer}')
    
    return answer


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    print("Example:")
    #print(checkio(5.85987448205))

    assert checkio(5.85987448205) == "e+pi"  # not pi+e (alphabetically order)
    assert checkio(18.2958548951) == "e**e+pi"
    assert checkio(47.6085189284) == "e**e*pi"
    assert checkio(5.85987448205) == 'e+pi'
    
    assert checkio(18.2958548951) == 'e**e+pi'
    assert checkio(47.6085189284) == 'e**e*pi'
    assert checkio(-0.42331082513) == 'e-pi'
    assert checkio(7.38905609893) == 'e*e'
    assert checkio(-2.48054830216) == 'e*e-pi*pi'
    assert checkio(57.9087276547) == 'e*pi**e-pi'
    assert checkio(0.07455076325) == 'e/pi**pi'
    assert checkio(0.10132118364) == 'e/e/pi/pi'
    
    assert checkio(3.14159265359) == 'pi'
    
    print("Coding complete? Click 'Check' to earn cool rewards!")