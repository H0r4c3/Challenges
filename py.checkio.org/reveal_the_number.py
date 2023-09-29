'https://py.checkio.org/en/mission/reveal-the-number/share/3ad546f708ca660ad4479724c62f9d77/'

'''
You are given a string of different characters (letters, digits and other symbols). 
The goal is to "extract" the number from the string: concatenate only digits, number sign and "." (if present) and 
return the result in number format. If no number can be extracted (no digits in the given string) - return None. 
Read preconditions below for some additional rules.

Expected behavior:

take into consideration the LAST number sign before the FIRST digit;
take into consideration the FIRST dot in the string (It's guaranteed, 
that it goes after at least one digit or has at least one digit after). 
If there is a dot, return as float, otherwise - integer.
'''

import re

def reveal_num(line: str) -> int | float | None:
    signs = re.findall('[+-]', line)
    print(signs)
    digits = re.findall('\d', line)
    print(digits)
    dots = re.findall('\.', line)
    print(dots)
    
    signs_digits_dots = re.findall('[+]|[-]|\d|[.]', line)
    print(f'signs_digits_dots = {signs_digits_dots}')
    
    if digits == []:
        return None
    
    if signs_digits_dots[0].isdigit() or signs_digits_dots[0] == '.':
        signs = ''
    
    if not signs and not dots:
        if digits[0] == 0:
            digits.pop(0)
        return int(''.join(digits))
    
    signs_digits_dots = re.findall('[+]|[-]|\d|[.]', line)
    print(f'signs_digits_dots = {signs_digits_dots}')
    
    digits_positions = [(pos, dig) for pos, dig in enumerate(signs_digits_dots) if dig.isdigit()]
    print(digits_positions)
    
    idx_first_digit = digits_positions[0][0]
    
    signs = [sign for sign in signs_digits_dots[:idx_first_digit] if sign in ['+', '-']]
    if signs: 
        sign = signs[-1]
    else:
        sign = ''
    
    print(signs)
    print(f'sign = {sign}')
    
    if sign == '+':
        sign = ''
    
    if '.' in signs_digits_dots:
        idx_first_dot = signs_digits_dots.index('.')
        print(idx_first_dot)
    
        first_digits = [dig for dig in signs_digits_dots[:idx_first_dot] if dig.isdigit()]
        print(first_digits)
        last_digits = [dig for dig in signs_digits_dots[idx_first_dot+1:] if dig.isdigit()]
        print(last_digits)
    
        result = sign + ''.join(first_digits) + '.' + ''.join(last_digits)
    else:
        result = sign + ''.join(digits)
    
    print(f'result = {result}')
    return eval(result)


# Best Solution: https://py.checkio.org/mission/reveal-the-number/publications/review/puzzle/

def reveal_num_(line:str, sub=__import__("re").sub):
    sign = sub(r'\D*(\+|-).*', r'\1', '+' + line)                  # get last sign before digit
    p1, *p2 = sub(r'[^0-9.]', r'', line).split('.')                # split numbers between dots
    return eval(f'{sign}{p1}.{"".join(p2)}') if p1 or p2 else None # get result


# Best Solution: 
# https://py.checkio.org/mission/reveal-the-number/publications/review/clear/

from re import findall

def reveal_num_(line: str) -> int | float | None:
    
    # Isolate a list of digits, decimals, and plus or minus signs.
    line = findall('[0-9\-\.\+]', line)[::-1]
    result = ''
    
    # Generate result from the end. I thought it made parsing for signs a little easier.
    for i, j in enumerate(line):
        
        # If this is a decimal, but any others are to come, ignore this.
        if j == '.' and '.' in line[i  + 1:]:
            continue
        
        # If it's a +/- sign, but any numbers are left to add OR a sign is already in the result, ignore this.
        if j in '-+' and (any(k.isdigit() for k in line[i+1:]) or any(k in result for k in '-+')):
            continue
        
        # Assuming first two conditions are passed, add a digit, decimal, or sign to the result.
        if j.isdigit() or j in '.-+':
            result += j
    
    # Flip it back around, take off stray positive or decimals, convert to float.  It'll be that, or None.
    return None if not len(result) else float(result[::-1].rstrip('.').lstrip('+'))


print("Example:")
print(reveal_num("+A%+-1-0..."))

# These "asserts" are used for self-checking
assert reveal_num("F0(t}") == 0
assert reveal_num("Utc&g") == None
assert reveal_num("-aB%|_-+2ADS.12+3.ADS1.2") == 2.12312
assert reveal_num("-aB%|_+-2ADS.12+3.ADS1.2") == -2.12312
assert reveal_num("zV№1}3;o.vEf``C.WqTY0") == 13.0
assert reveal_num("!3B'j=(}89JQ6aWvN*%5@uy.r)B<?pZ.!545ZD^KF9Sx@gqfa*") == 38965.5459
assert reveal_num('!#iHL}wcI?KR=X!gF0d&S-1zj&LgJ!`tzbn#mEPV7mL&R2f)W') == 172

print("The mission is done! Click 'Check Solution' to earn rewards!")