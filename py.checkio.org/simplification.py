'https://py.checkio.org/en/mission/simplification/'

'''
You are given a mathematical expression with brackets and one variable as a string. 
The expression contains "x", brackets and the following operators: + - * . 
You should convert this to a Polynomial. The power of "x" should be represented by "**".

The final form of the polynomial should be in the following format:

     CN*x**n+CN1*x**(n-1)+...+C1*x+C0
'''
from sympy import sympify

def simplify_(expr):
    # convert expr to a type that can be used inside sympy
    new_expr = sympify(expr)
    print(new_expr)
    
    # expand the polynomial expression
    new_expr_exp = new_expr.expand()
    print(new_expr_exp)
    
    # convert to string, in order to eliminate the spaces using replace()
    result = str(new_expr_exp).replace(' ', '')
    print(result)
    
    return result


def simplify(expr):
    # expand the polynomial expression
    new_expr_exp = expand(expr)
    print(new_expr_exp)
    
    # convert to string, in order to eliminate the spaces using replace()
    result = str(new_expr_exp).replace(' ', '')
    print(result)
    
    return result


# Best Solution: 
# https://py.checkio.org/mission/simplification/publications/Pouf/python-3/expandreplace/?ordering=most_voted&filtering=all

from sympy import expand

def simplify_(expr: str) -> str:
    return str(expand(expr)).replace(" ", "")


# Best Solution: 
# https://py.checkio.org/mission/simplification/publications/_Chico_/python-3/first/share/b6a9d85fa6f629b4313bfd962eba73b1/

from sympy import sympify

def simplify_(expr):
    expr = sympify(expr)
    return str(expr.expand()).replace(" ","")


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert simplify("(x-1)*(x+1)") == "x**2-1", "First and simple"
    assert simplify("(x+1)*(x+1)") == "x**2+2*x+1", "Almost the same"
    assert simplify("(x+3)*x*2-x*x") == "x**2+6*x", "Different operations"
    assert simplify("x+x*x+x*x*x") == "x**3+x**2+x", "Don't forget about order"
    assert simplify("(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6", "All together"
    assert simplify("x*x-(x-1)*(x+1)-1") == "0", "Zero"
    assert simplify("5-5-x") == "-x", "Negative C1"
    assert simplify("x*x*x-x*x*x-1") == "-1", "Negative C0"
    print('Done!!!')