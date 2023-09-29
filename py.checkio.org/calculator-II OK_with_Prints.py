'https://py.checkio.org/en/mission/calculator-ii/share/8bf6e28b9dfe841548135283262159b9/'

'''
Expected behavior:

1. beginning zeros should be removed, only-zeros number - converted to single zero;
2. among +- signs between numbers, the last one should be taken;
3. "==" means repeating the last operation;
4. "+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself).
'''

# My Solution:

import re

def left_strip_zeros_and_plus(log):
    '''
    beginning zeros should be removed, only-zeros number - converted to single zero
    '''
    new_log = log
    for char in log:
        if char in ['0', '+']:
            new_log = log.lstrip(char)
        else:
            break
        
    if new_log in ('+', '-', '*', '/', ''):
        return '0'
    
    return new_log
    

def replace_number_and_minus_or_plus_before_equal(log):
    '''
    "+=" or "-=" - adding/subtracting the number (or operations result) 
    before the combination (doubling the number/subtracting itself)
    '''
    pattern = r'(\d+)([\-\+])='
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    digits = match.group(1)
    op = match.group(2)
    log = re.sub(pattern, digits + op + digits + '=', log)
    
    print(f'log after replace_number_and_minus_or_plus_before_equal is {log}')
    return log


def repeating_the_last_operation(log):
    '''
    "==" means repeating the last operation
    '''
    # The pattern has 3 groups: (digit) (operation) (==)
    pattern = r'([\+\-\*\/]+)(\d*)(={2})'
    match = re.search(pattern, log)
    if match == None:
        return log
    print(f'The match before == is {match.group()}')
    op, digits, equals = match.group(1), match.group(2), match.group(3)
    log = log.replace(op + digits + equals, op + str(int(digits)*2) + '=')
    print(f'log after replacing == with {op + digits + "="} is {log}')
    
    if '==' in log:
        repeating_the_last_operation(log)
    else:
        return log
    

def replace_signs_with_last(log):
    '''
    among +- signs between numbers, the last one should be taken;
    '''
    pattern = r'(\d+)([\+\-]+[\+\-]+)(\d+)'
    match = re.search(pattern, log)
    
    if not match:
        return log
        
    print(f'The match for +- signs is {match.group(0)}')

    last_sign = match.group(2)[-1]
    print(f'last_sign is {last_sign}')
    digits1, signs, digits2 = match.group(1), match.group(2), match.group(3)
    print(f'signs are {signs}')
    log = log.replace(signs, last_sign)
    
    match = re.search(pattern, log)
    print(f'new match for +- is {match}')
    if match:
        replace_signs_with_last(log)
    else:
        print(f'log after replace_signs_with_last is {log}')
        return log
    

def replace_equal_and_signs_at_end(log):
    '''
    =+ or =- at end of the log
    -=-+3-++--+-2=-
    '''
    pattern = r'=[\-\+]+$'
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    print(f'match in replace_equal_and_signs_at_end is {match.group()}')
    log = log.replace(match.group(), '=')
    
    match = re.search(pattern, log)
    if match:
        log = replace_equal_and_signs_at_end(log)
    else:
        print(f'log after replace_equal_and_signs_at_end is {log}')
        return log


def replace_digits_sign_digits_equal(log):
    '''
    2+3=7+7=
    '''
    pattern = r'\d+[\-\+]+\d+='
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        log = log.replace(match.group(), str(eval(match.group()[:-1])) + '+')
        print(f'log after replace_digit_sign_digit_equal is {log}')
        return log


def replace_digits_sign_digits_sign_equal_at_start(log):
    '''
    3+2-=
    '''
    pattern = r'^(\d+[\-\+]+\d+)([\+\-])='
    match = re.search(pattern, log)
    
    if match == None:
        return log
    
    print(f'match = {match.group()}')
    log = log.replace(match.group(), str(eval(match.group(1))) + match.group(2) + '=')
    print(f'log after replace_digits_sign_digits_sign_equal_at_start is {log}')
    
    match = re.search(pattern, log)
    if match:
        log = replace_digits_sign_digits_sign_equal_at_start(log)
    else:
        print(f'log after replace_digits_sign_digits_sign_equal_at_start is {log}')
        return log
    
    
def find_last_plus_or_minus(string_before_digit):
    '''
    find the last sign before digit (+ or -):
    '''
    # if = is in string_before_digit, slice the part till =
    match_equal = re.search(r'\=', string_before_digit)
    if match_equal:
        pos_equal = match_equal.start()
        print(f'match_equal is {pos_equal}')
        string_before_digit = string_before_digit[pos_equal+1:]
        print(f'string_before_digit after slice using pos_equal is {string_before_digit}')
        if match_equal == None:
            return None
    
    match = re.findall(r'[+-][^+-]*$', string_before_digit)
    if match:
        return match[-1]
    else:
        return None
    

def replace_equal_and_signs_at_beginning(log):
    pattern = r'\d'
    first_digit = re.search(pattern, log)
    print(first_digit)
    pos = first_digit.start()
    
    print(f'Position of the first digit is {pos}')
    string_before_digit = log[:pos]
    print(f'string_before_digit is {string_before_digit}')
    last_sign = find_last_plus_or_minus(string_before_digit)
    print(f'last_sign is {last_sign}')
    
    if last_sign == None:
        return log[pos:]
    
    # replace string_before_digit with last_sign
    log = log.replace(string_before_digit, last_sign, 1)    
    print(f'log after replace_equal_and_signs_at_beginning is {log}')
    return log
    

def replace_equal_and_digit(log):
    pattern = r'=(\d+)'
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        pos = match.start()
        print(f'log after replace_equal_and_digit is {log[pos+1:]}')
        return log[pos+1:]
    
    

def calculator(log: str) -> str:
    print(f'The starting log is {log}')
    
    log = left_strip_zeros_and_plus(log)
    log = replace_digits_sign_digits_sign_equal_at_start(log)
    log = repeating_the_last_operation(log)
    log = replace_number_and_minus_or_plus_before_equal(log)
    log = replace_signs_with_last(log)
    log = replace_equal_and_signs_at_end(log)
    log = replace_equal_and_signs_at_beginning(log)
    log = replace_equal_and_digit(log)
    log = replace_digits_sign_digits_equal(log)
    
    print(f'New log after the 7 replacements: {log}')
    
    if log.isdigit():
        print(f'log is digit = {log}')
        return log
    
    if log[-1] not in ('=', '+', '-', '*', '/'):
        try:
            log = re.search(r'[1-9]+$', log).group()
        except AttributeError:
            return '0'
    else:
        print(f'new log is: {log}')
        print(f'eval')
        log = str(eval(log[:-1]))
    
    result = log
    print(f'result = {result}')
    
    return log if log else '0'



# Best Solution: 
# https://py.checkio.org/mission/calculator-ii/publications/CDG.Axel/python-3/could-12-lines-proc-be-clear/?ordering=most_voted&filtering=all

def calculator_(log: str) -> str:
    second, screen, new, op, magic = 0, 0, True, '=', lambda: (screen, -screen)[op == '-']

    for key in log:
        if key.isdigit():
            screen = screen * 10 * (not new) + int(key)
        elif key in '+-':
            second = screen = screen if op == '=' or new else second + magic()
        elif key == '=' == op:
            screen = screen + second
        elif key == '=':
            screen = (second, screen)[new] + (second := magic())
        op = (op, key)[new := key in '+-=']

    return str(screen)


print("Example:")
#print(calculator("3+="))

# These "asserts" are used for self-checking
print(f'---0.---')
assert calculator("13+14=") == "27"
print(f'---1.---')
assert calculator("3+=") == "6"
print(f'---2.---')
assert calculator("3+2==") == "7"
print(f'---3.---')
assert calculator("4-1==") == "2"
print(f'---4.---')
assert calculator("3+-2=") == "1"
print(f'---5.---')
assert calculator("-=-+3-++--+-2=-") == "1"
print(f'---6.---')
assert calculator("000000") == "0"
print(f'---7.---')
assert calculator("00001234") == "1234"
print(f'---8.---')
assert calculator("12") == "12"
print(f'---9.---')
assert calculator("+12") == "12"
print(f'---10.---')
assert calculator("") == "0"
print(f'---11.---')
assert calculator("1+2") == "2"
print(f'---12.---')
assert calculator("2+") == "2"
print(f'---13.---')
assert calculator("1+2=") == "3"
print(f'---14.---')
assert calculator("1+2-") == "3"
print(f'---15.---')
assert calculator("1+2=2") == "2"
print(f'---16.---')
assert calculator("=5=10=15") == "15"
print(f'---17.---')
assert calculator('78-=') == "0"
print(f'---18.---')
assert calculator('+-=12=') == '12'
print(f'---19.---')
assert calculator('2+3=7+7=') == '14'
print(f'---20.---')
assert calculator('2+3=+7=') == '12'
print(f'---21.---')
assert calculator('+1+2+3+4=') == '10'
print(f'---22.---')
assert calculator('3+2-=') == '0'

print("The mission is done! Click 'Check Solution' to earn rewards!")