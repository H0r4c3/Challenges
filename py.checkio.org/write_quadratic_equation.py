'https://py.checkio.org/en/mission/write-quadratic-equation/'

'''
This is what you should do in this mission. You have input list with integers - a, x1 [, x2]. 
If it has length 2, it means, x1 == x2: equation has two equal roots (one distinct root). 
You function should return quadratic equation as a string. Pay attention to specific cases.
'''
import re

def quadr_equation(data: list[int]) -> str:
    
    if len(data) == 3:
        a, x1, x2 = data 
    else:
        a, x1 = data
        x2 = x1
    
    b = a * (x1 + x2)
    print(f'b = {b}') 
    
    c = a * x1 * x2
    print(f'c = {c}')
        
    if b > 0:
        if c > 0:
            result = f'{a}*x**2 - {abs(b)}*x + {abs(c)} = 0'
        if c < 0:
            result = f'{a}*x**2 - {abs(b)}*x - {abs(c)} = 0'
        elif c == 0:
            result = f'{a}*x**2 - {abs(b)}*x = 0'
    elif b < 0:
        if c > 0:
            result = f'{a}*x**2 + {abs(b)}*x + {abs(c)} = 0'
        if c < 0:
            result = f'{a}*x**2 + {abs(b)}*x - {abs(c)} = 0'
        elif c == 0:
            result = f'{a}*x**2 + {abs(b)}*x = 0'
    elif b == 0:
        if c > 0:
            result = f'{a}*x**2 + {abs(c)} = 0'
        if c < 0:
            result = f'{a}*x**2 - {abs(c)} = 0'
        elif c == 0:
            result = f'{a}*x**2 = 0'
      
    if a == 1:
        result = re.sub('1\*', '', result)
    elif a == -1:
        result = re.sub('-1\*', '-', result)
        
     
    print(result)
    return result


print("Example:")
#print(quadr_equation([2, 4, 6]))

assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
assert quadr_equation([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"
assert quadr_equation([2, 0]) == "2*x**2 = 0"
assert quadr_equation([2, 4]) == "2*x**2 - 16*x + 32 = 0"
assert quadr_equation([1, 0]) == 'x**2 = 0'
assert quadr_equation([-1, 0]) == '-x**2 = 0'

print("The mission is done! Click 'Check Solution' to earn rewards!")