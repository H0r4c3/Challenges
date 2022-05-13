'https://py.checkio.org/en/mission/max-digit/'

'''
You have a number and you need to determine which digit in this number is the biggest.
'''

def max_digit(number: int) -> int:
    my_list = str(number)
        
    result = int(max(my_list))
    
    print(result)
    return result


# My Solution using namedtuple (for the Quest)
from collections import namedtuple

def max_digit_(number: int) -> int:
    Number = namedtuple('Number', ['nr'])
    n = Number(number)
    numb = str(n.nr)
        
    print(max(numb))


# Best Solution: 
# https://py.checkio.org/mission/max-digit/publications/veky/python-3/chu-chu/?ordering=most_voted&filtering=all

max_digit_ = lambda number: int(max(str(number)))


if __name__ == '__main__':
    print("Example:")
    #print(max_digit(52))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")