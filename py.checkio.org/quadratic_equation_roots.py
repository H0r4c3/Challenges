'https://py.checkio.org/en/mission/quadratic-equation-roots/'

'''
A quadratic equation is represented as ax2 + bx + c = 0. The general formula to find its roots (x-values for which y = 0) is:

example

This formula provides two roots: x1, x2. The value inside the square root, b2-4ac is known as the discriminant (D). 
Based on the value of the discriminant, a quadratic equation can have:

two distinct real roots (D > 0);
one real root (D = 0);
no real roots (D < 0).
Your code must return Iterable containing two values: the roots x1, x2, sorted descending. 
f there's only one real root, both values will be the same. If there are no real roots, the Iterable should contain the string "No real roots".
'''

from collections.abc import Iterable
from typing import Union
from math import sqrt


def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:
    print(f'START: {(a, b, c)}')
    discriminant = b**2 - 4 * a * c
    print(f'discriminant = {discriminant}')
    
    if discriminant < 0:
        print("No real roots")
        return ["No real roots"]
    else:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
    result = sorted([x1, x2], reverse=True)
    print(result)
    return result


print("Example:")
print(list(quadratic_roots(1, 2, 3)))

# These "asserts" are used for self-checking
assert list(quadratic_roots(1, -3, 2)) == [2, 1]
assert list(quadratic_roots(1, 0, -1)) == [1, -1]
assert list(quadratic_roots(1, 2, 1)) == [-1, -1]
assert list(quadratic_roots(1, 0, 1)) == ["No real roots"]
assert list(quadratic_roots(1, 4, 4)) == [-2, -2]
assert list(quadratic_roots(1, -5, 6)) == [3, 2]
assert list(quadratic_roots(1, -6, 9)) == [3, 3]
assert list(quadratic_roots(2, 2, 1)) == ["No real roots"]
assert list(quadratic_roots(2, -7, 6)) == [2, 1.5]
assert list(quadratic_roots(2, -3, 1)) == [1, 0.5]

print("The mission is done! Click 'Check Solution' to earn rewards!")