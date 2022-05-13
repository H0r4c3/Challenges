'https://py.checkio.org/en/mission/funny-adding/'

'''
We have an array of two positive integers. Add these two numbers together.
'''
# My Solution (using reduce)
from functools import reduce

def checkio(data):
    """The sum of two positive integer elements"""
    a, b = data
    
    if a | b < 0:
        raise Exception('Only positive integers accepted!!!')
    
    return reduce(lambda a, b: a + b, data)



# Another My Solution (using enum.Enum):
from enum import Enum

def checkio(data):
    """The sum of two integer elements"""
    a, b = data
    class Numbers(Enum):
        ONE = a
        TWO = b

    print(Numbers.ONE.value + Numbers.TWO.value)
    return Numbers.ONE.value + Numbers.TWO.value


    
if __name__ == '__main__':
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7, 1]) == 8, 'Second'
    #assert checkio([-7, 1]) == Exception, 'Exception'
    print('All ok')