'https://py.checkio.org/en/mission/brackets/'

'''
You are given an expression with numbers, brackets and operators. 
For this task only the brackets matter. 
Brackets come in three flavors: "{}" "()" or "[]".

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).
'''
import re

def check(my_string):
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        print(list(x in my_string for x in brackets))
        for br in brackets:
            my_string = my_string.replace(br, '')
            print(my_string)
    return not my_string

def checkio(expression):
    
    my_brackets = re.findall('[(){}[\]]', expression)
    print(f'my_brackets = {my_brackets}')
    
    my_string = ''.join(my_brackets)
    
    return check(my_string)


# Best Solution: 
# https://py.checkio.org/mission/brackets/publications/texom512/python-3/simple-and-only-5-lines/?ordering=most_voted&filtering=all

def checkio(str):
    str = ''.join([c for c in str if c in '()[]{}'])
    print(str)
    
    while any(b in str for b in ('()', '[]', '{}')):
        str = str.replace('()', '').replace('[]', '').replace('{}', '')

    return not str



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    #assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    print('Done!!!')

