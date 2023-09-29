'https://py.checkio.org/en/mission/can-balance/'

'''
Each item in the list of items is considered to be a physical weight, and guaranteed to be a positive integer. 
Your task is to find and return a fulcrum position in this list so that when balanced on that position, 
the total torque of the items to the left of that position equals the total torque of the items to the right of that position.
'''

from typing import Iterable

def can_balance(weights: Iterable) -> int:
    # your code here
    return -1



# Best Solution:
# https://py.checkio.org/mission/can-balance/publications/juestr/python-3/analytical/share/61b2c8c3322b2d914a9e912f6704559e/

from typing import Iterable

def can_balance(weights: Iterable) -> int:
    # torque == sum((i - p) * w for i, w in enumerate(weights)) == 0
    # ==>  sum(i*w_i) - sum(p*w_i) == 0
    # ==>  sum(i*w_i) - p*sum(w_i) == 0
    # ==>  p == sum(i*w_i)/sum(w_i)

    p = sum(i*w for i, w in enumerate(weights)) / sum(weights)
    return int(p) if int(p) == p else -1


if __name__ == '__main__':
    print("Example:")
    print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")