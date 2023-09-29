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

def remove_leading_zeros(log):
    '''
    beginning zeros should be removed, only-zeros number - converted to single zero
    '''
    log = re.sub(r'\b0+([1-9]*)', r'\1', log)
    
    if log in ('+', '-', '*', '/', '', None):
        return '0'
    else:
        return log


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
    
    op, digits, equals = match.group(1), match.group(2), match.group(3)
    log = log.replace(op + digits + equals, op + str(int(digits)*2) + '=')
    
    
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
        
    last_sign = match.group(2)[-1]
    digits1, signs, digits2 = match.group(1), match.group(2), match.group(3)
    log = log.replace(signs, last_sign)
    match = re.search(pattern, log)
    
    if match:
        replace_signs_with_last(log)
    else:
        
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
    
    log = log.replace(match.group(), '=')
    match = re.search(pattern, log)
    if match:
        log = replace_equal_and_signs_at_end(log)
    else:
        
        return log


def replace_digit_sign_digit_equal(log):
    '''
    2+3=7+7=
    '''
    pattern = r'\d+[\-\+]+\d+='
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        log = log.replace(match.group(), str(eval(match.group()[:-1])) + '+')
        
        return log
    
def replace_digits_sign_digits_sign_equal_at_start(log):
    '''
    3+2-=
    '''
    pattern = r'^(\d+[\-\+]+\d+)([\+\-])='
    match = re.search(pattern, log)
    
    if match == None:
        return log
    
    log = log.replace(match.group(), str(eval(match.group(1))) + match.group(2) + '=')
    
    match = re.search(pattern, log)
    if match:
        log = replace_digits_sign_digits_sign_equal_at_start(log)
    else:
        return log
     
    
def find_last_plus_or_minus(string_before_digit):
    '''
    find the last sign before digit (+ or -):
    '''
    # if = is in string_before_digit, slice the part till =
    match_equal = re.search(r'\=', string_before_digit)
    if match_equal:
        pos_equal = match_equal.start()
        string_before_digit = string_before_digit[pos_equal+1:]
        
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
    pos = first_digit.start()
    string_before_digit = log[:pos]
    last_sign = find_last_plus_or_minus(string_before_digit)
    
    if last_sign == None:
        return log[pos:]
    
    # replace string_before_digit with last_sign
    log = log.replace(string_before_digit, last_sign, 1)    
    
    return log
    

def replace_equal_and_digit(log):
    pattern = r'=(\d+)'
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        pos = match.start()    
        return log[pos+1:]
    
    
def calculator(log: str) -> str:
    print(log)
    log = remove_leading_zeros(log)
    log = repeating_the_last_operation(log)
    log = replace_number_and_minus_or_plus_before_equal(log)
    log = replace_signs_with_last(log)
    log = replace_equal_and_signs_at_end(log)
    log = replace_equal_and_signs_at_beginning(log)
    log = replace_equal_and_digit(log)
    log = replace_digit_sign_digit_equal(log)
    print(log)
    
    if log.isdigit():
        return log
    
    if log[-1] not in ('=', '+', '-', '*', '/'):
        try:
            log = re.search(r'[1-9]+$', log).group()
        except AttributeError:
            return '0'
    else:
        log = str(eval(log[:-1]))
    
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


#

# These "asserts" are used for self-checking

assert calculator("13+14=") == "27"

assert calculator("3+=") == "6"

assert calculator("3+2==") == "7"

assert calculator("4-1==") == "2"

assert calculator("3+-2=") == "1"

assert calculator("-=-+3-++--+-2=-") == "1"

assert calculator("000000") == "0"

assert calculator("00001234") == "1234"

assert calculator("12") == "12"

assert calculator("+12") == "12"

assert calculator("") == "0"

assert calculator("1+2") == "2"

assert calculator("2+") == "2"

assert calculator("1+2=") == "3"

assert calculator("1+2-") == "3"

assert calculator("1+2=2") == "2"

assert calculator("=5=10=15") == "15"

assert calculator('78-=') == "0"

assert calculator('+-=12=') == '12'

assert calculator('2+3=7+7=') == '14'

assert calculator('2+3=+7=') == '12'

assert calculator('000005+003=') == '8'

assert calculator('+1+2+3+4=') == '10'

print('Done!')