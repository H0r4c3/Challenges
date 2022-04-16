'https://py.checkio.org/en/mission/solution-for-anything/'

'''
We need a solution which can pass any case. The result of your solution should pass for any comparison with anything.

You should write the function "checkio" which is called with one argument, the result will be compared with some other data (==, !=, etc) and 
the result of that comparison should be True.

Input: Some data. Maybe that data over there.

Output: The something as a something-else.
'''

def checkio(anything):
    """
        try to return anything else :)
    """
    return True


# Best Solution: 
# https://py.checkio.org/mission/solution-for-anything/publications/Sim0000/python-3/first/share/bddc7370009d25c823d3ee6b862c9e23/

def checkio(anything):
    class T:
        __lt__=__gt__=__le__=__ge__=__eq__=__ne__ = lambda a, b: True
        
    return T()


if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')