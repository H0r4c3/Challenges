'https://py.checkio.org/en/mission/gcd/'

'''
"[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day."
-- Donald Knuth, The Art of Computer Programming, Vol. 2: Seminumerical Algorithms, 2nd edition (1981).

The greatest common divisor (GCD), also known as the greatest common factor of two or more integers (at least one of which is not zero), is the largest positive integer that divides a number without a remainder. For example, the GCD of 8 and 12 is 4.

You are given an arbitrary number of positive integers. You should find the greatest common divisor for these numbers.

Input: An arbitrary number of positive integers.

Output: The greatest common divisor as an integer.
'''

import math

def greatest_common_divisor(*args:int) -> int:
    
    return math.gcd(*args)


if __name__ == '__main__':
    print("Example:")
    print(greatest_common_divisor(6, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert greatest_common_divisor(6, 4) == 2
    assert greatest_common_divisor(2, 4, 8) == 2
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1
    assert greatest_common_divisor(3, 9, 3, 9) == 3