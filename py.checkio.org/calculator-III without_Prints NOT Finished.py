'https://py.checkio.org/en/mission/calculator-iii/'

'''
Expected behavior:

1. beginning zeros should be removed, only-zeros number - converted to single zero;
2. among +- signs between numbers, the last one should be taken;
3. "==" means repeating the last operation;
4. "+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself);
5. the calculator ignores digit you enter after 5th;
6. "-" for numbers < 0 is NOT taking digit place;
7. if the abs(result) is more than 99999 - "error" is shown as a result.
'''

# My Solution

import re


def left_strip_zeros(log):
    '''
    beginning zeros should be removed, only-zeros number - converted to single zero
    
    000005+003
    '''
    pattern = r'\b(0+)(\d+)'
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    log = log.replace(match.group(), match.group(2))
    
    match = re.search(pattern, log)
    
    if match:
        log = left_strip_zeros(log)
    else:
        print(f'log after left_strip_zeros is {log}')
    
    return log
    
    
def truncate_digits(log):
    'the calculator ignores digit you enter after 5th'
    pattern = r'(\d{6,})'
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    log = log.replace(match.group(), match.group()[:5])
    
    match = re.search(pattern, log)
    
    if match:
        log = truncate_digits(log)
    else:
        return log
    
    
    return log


def replace_digits_equal_sign_digits(log):
    pattern = r'(\d+)(\=)([\+\-])(\d+)'
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    log = log.replace(match.group(), str(match.group(1) + match.group(3) + match.group(4)))
    
    match = re.search(pattern, log)
    
    if match:
        log = replace_digits_equal_sign_digits(log)
    else:
        print(f'log after replace_digits_equal_sign_digits is {log}')
    
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
    log = log.replace(op + digits + equals, op + str(int(digits)*2) + '=') if int(digits)*2 < 99999 else 'error'
         
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


def replace_digits_sign_digits_equal_digits(log):
    '''
    2+3=7+7=
    '''
    pattern = r'(\d+[\-\+]+\d+=)(\d+)'
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        log = log.replace(match.group(), match.group(2))
        #log = log.replace(match.group(), str(eval(match.group()[:-1]+)))
        return log


def replace_digits_sign_digits_equal_or_sign(log):
    '''
    1+2=
    Be careful, check, maybe after = is another = 
    '''
    pattern = r'(\d+[\-\+]+\d+[=\-\+])'
    match = re.search(pattern, log)
    pattern_equals = r'(\d+[\-\+]+\d+==)'
    match_equals = re.search(pattern_equals, log)
    
    if (not match) or (match_equals):
        return log
    
        
    if abs(eval(match.group()[:-1])) > 99999:
        return 'error'
    
    log = log.replace(match.group(), str(eval(match.group()[:-1])))
    
    match = re.search(pattern, log)
    
    if match:
        log = replace_digits_sign_digits_equal_or_sign(log)
    
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
    if not first_digit:
        return log
    pos = first_digit.start()
    
    string_before_digit = log[:pos]
    last_sign = find_last_plus_or_minus(string_before_digit)
        
    if last_sign == None:
        return log[pos:]
    
    # replace string_before_digit with last_sign
    log = log.replace(string_before_digit, last_sign, 1)    
    return log
    

def replace_sign_or_equal_and_digit_at_end(log):
    pattern = r'[\+\-=](\d+)$'
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        pos = match.start()
        return log[pos+1:]
    
    
def replace_digits_and_sign_at_end(log):
    pattern = r'(\d+)[\+\-=]$'
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        log = log.replace(match.group(), match.group(1))
        return log
    
    
def calculator(log: str) -> str:
    if log == '': return '0'
        
    log = left_strip_zeros(log)
    log = truncate_digits(log)
    log = replace_digits_equal_sign_digits(log)
    log = replace_digits_sign_digits_sign_equal_at_start(log)
    log = replace_number_and_minus_or_plus_before_equal(log)
    log = repeating_the_last_operation(log)
    log = replace_signs_with_last(log)
    log = replace_equal_and_signs_at_end(log)
    log = replace_equal_and_signs_at_beginning(log)
    log = replace_sign_or_equal_and_digit_at_end(log)
    log = replace_digits_sign_digits_equal_digits(log)
    log = replace_digits_sign_digits_equal_or_sign(log)
    log = replace_digits_and_sign_at_end(log)
    
    if log=='error' or abs(int(log)) > 99999:
        return 'error'
    
    if log.isdigit():
        return log
    
    if log[-1] not in ('=', '+', '-', '*', '/'):
        try:
            log = re.search(r'[1-9]+$', log).group()
        except AttributeError:
            return '0'
    else:
        log = str(eval(log[:-1]))
    
    result = log
        
    return log if log else '0'


##
# These "asserts" are used for self-checking
assert calculator("90000+10000=") == "error"
assert calculator("90000+10000-10000=") == "error"
assert calculator("90000+10000-10000") == "10000"
assert calculator("123456789") == "12345"
assert calculator("123456789+5=") == "12350"
assert calculator("5+123456789") == "12345"
assert calculator("50000+=") == "error"
assert calculator("3+=") == "6"
assert calculator("3+2==") == "7"
assert calculator("4-1==") == "2"
assert calculator("3+-2=") == "1"
assert calculator("-=-+3-++--+-2=-") == "1"
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"
assert calculator("") == "0"
assert calculator("1+2") == "2"
assert calculator("2+") == "2"
assert calculator("1+2=") == "3"
assert calculator("1+2-") == "3"
assert calculator("1+2=2") == "2"
assert calculator("=5=10=15") == "15"
assert calculator('50000-====') == 'error'
assert calculator('2+3=+7=') == '12'
assert calculator('000005+003') == '3'
assert calculator('-5-10+15-') == '0'
assert calculator('+1+2+3+4=') == '10'
assert calculator('+') == '0'

print("The mission is done! Click 'Check Solution' to earn rewards!")