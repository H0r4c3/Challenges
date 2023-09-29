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

TESTS = {
    "Basics": [
        {"input": [5.85987448205], "answer": 'e+pi'},
        {"input": [18.2958548951], "answer": 'e**e+pi'},
        {"input": [47.6085189284], "answer": 'e**e*pi'},
        {"input": [-0.42331082513], "answer": 'e-pi'},
        {"input": [7.38905609893], "answer": 'e*e'},

    ],
    "Extra": [
        {"input": [-2.48054830216], "answer": 'e*e-pi*pi'},
        {"input": [57.9087276547], "answer": 'e*pi**e-pi'},
        {"input": [0.07455076325], "answer": 'e/pi**pi'},
        {"input": [0.10132118364], "answer": 'e/e/pi/pi'},

    ]
}

import logging

from math import e, pi, isclose
from itertools import combinations, combinations_with_replacement, permutations

LOG_PATH = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\py.checkio.org\e+pi.log'

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=LOG_PATH, 
                    filemode='w')

def find_arithmetic_expression():
    '''
    Brute-force: generate all possible arithmetic expressions using e and pi
    '''
    operators_comb_all = list()
    expressions = list()
    operands = ['e', 'pi']
    operators = ['+', '-', '*', '/', '**']
    #operators_double = [('+', '+'), ('-', '-'), ('*', '*'), ('/', '/'), ('**', '**')]
    #operators_triple = [('+', '+', '+'), ('-', '-', '-'), ('*', '*', '*'), ('/', '/', '/'), ('**', '**', '**')]
    
    # all combinations from operands list
    operands_all = [('e', 'e'), ('pi', 'pi'), ('e', 'pi'), ('pi', 'e'), 
                 ('e', 'e', 'pi'), ('pi', 'pi', 'e'), ('e', 'pi', 'pi'), ('pi', 'e', 'e'), 
                 ('e', 'e', 'pi', 'pi'), ('pi', 'pi', 'e', 'e'), ('e', 'pi', 'e', 'pi'), ('pi', 'e', 'pi', 'e')]
    
    # all combinations from operators list
    for rep in range(1, 4):
        operators_comb = list(combinations_with_replacement(operators, rep))
        print(operators_comb)
        logging.debug(f'operators_comb = {operators_comb}')
        for item in operators_comb:
            perm_item = set(permutations(item, rep))
            operators_comb_all.extend(perm_item)
    print(f'operators_comb_all = {operators_comb_all}')
    logging.debug(f'operators_comb_all = {operators_comb_all}')
    
    # combine operands with operators
    for operands in operands_all:
        for operators in operators_comb_all:
            if len(operands) == len(operators) + 1:
                expression = intercalation(operands, operators)
                #print(expression)
                expressions.append(expression)
    expressions.insert(0, 'e')
    expressions.insert(0, 'pi')
    print(expressions)
    #logging.debug(f'expressions = {expressions}')
            
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
    answers = list()
    for expression in expressions:
        print(f'expression = {expression}')
        try:
            value = eval(expression)
            print(f'expression = {expression} = {value}')
            #logging.debug(f'expressions = {expressions} = {value}')
            if isclose(value, result, rel_tol=1e-10):
                answers.append(expression)
        except ZeroDivisionError as e:
            print('A ZeroDivisionError occurred:', e)
            logging.info(f'A ZeroDivisionError occurred: {e}')
        except OverflowError as e:
            print('OverflowError occurred:', e)
            logging.info(f'OverflowError occurred: {e}')
            
    answers = sorted(answers, key=len)
    print(f'answers = {answers}')
    logging.debug(f'answers = {answers}')
    
    return answers[0]
    

def checkio(n: float) -> str:
    #from math import e, pi
    
    #print(e) #2.718281828459045
    #print(pi) #3.141592653589793
    
    print(f'START: {n}')
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