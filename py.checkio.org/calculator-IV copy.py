'https://py.checkio.org/en/mission/calculator-iv/'

'''
Expected behavior:

beginning zeros should be removed, only-zeros number - converted to single zero;
among +- signs between numbers, the last one should be taken;
"==" means repeating the last operation;
"+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself);
the calculator ignores digit you enter after 5th;
"-" for numbers < 0 is NOT taking digit place;
if the abs(result) is more than 99999 - "error" is shown as a result;
for float, if the integer part of abs(result) is more then 9999 - "error" is shown as a result;
for float, in case the total length of number is more than 5 digits, it should be rounded to 5 digits (1.23456 -> 1.235);
for float, beginning and trailing zeros should be removed (until the "." if possible): 0.1200 -> .12 , 123.00 -> 123. ;
It should be done after the rounding: 1.000123 -> 1. . Stripping of trailing zeros should only be done after entering a number has concluded (non-digit character 
pressed).

Steps for float:
- if the integer part of abs(result) is more then 9999 - "error" is shown as a result
- if the total length of number is more than 5 digits, it should be rounded to 5 digits (1.23456 -> 1.235)
- if non-digit character is pressed, beginning and trailing zeros should be removed (until the "." if possible): 0.1200 -> .12 , 123.00 -> 123
'''
# sys.path.append(r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Decorators')

#import sys
import re
from decimal import Decimal
#from timer_decorator import timer




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
    
    print(f'log after left_strip_zeros_and_plus is {new_log}')
    
    return new_log


def left_strip_zeros(log):
    '''
    beginning zeros should be removed, only-zeros number - converted to single zero
    
    000005+003
    000000
    '''
    print(f'Starting left_strip_zeros')
    pattern1 = r'^(0+)(\d*\.?\d+)'
    pattern2 = r'([\+\-])(0+)(\d*\.?\d+)'
    match1 = re.search((pattern1), log)
    match2 = re.search((pattern2), log)
    
    if not (match1 or match2):
        return log
    
    if match1:
        print(f'match.group() in left_strip_zeros = {match1.group()}')
        log = log.replace(match1.group(), match1.group(2))
        
    if match2:
        print(f'match.group() in left_strip_zeros = {match2.group()}')
        log = log.replace(match2.group(), match2.group(1) + match2.group(3))
    
    match1 = re.search((pattern1), log)
    match2 = re.search((pattern2), log)
    
    if match1 or match2:
        log = left_strip_zeros(log)
    else:
        print(f'log after left_strip_zeros is {log}')
    
    return log
    
    
def truncate_digits(log):
    '''the calculator ignores digit you enter after 5th'''
    print(f'Starting truncate_digits')
    pattern = r'(\d){6,}[^.]'
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    log = re.sub(match.group(), match.group()[:5], log)
    #log = log.replace(match.group(), match.group()[:5])
    
    match = re.search(pattern, log)
    
    if match:
        log = truncate_digits(log)
    else:
        print(f'log after truncate_digits is {log}')
        return log
    
    return log


def round_to_5_digits(log):
    print(f'Starting round_to_5_digits')
    pattern = r'(\d){6,}'
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        log = log[:5]
        print(f'log after round_to_5_digits is {log}')
        return log
    

def round_to_5_digits_float(log):
    '''
    For float, in case the total length of number is more than 5 digits, it should be ROUNDED to 5 digits (1.23456 -> 1.235)
    
    assert calculator("0001.1000") == "1.100"
    '''
    print(f'Starting round_to_5_digits_float using as log {log}')
    pattern = r'^(\d*)(\.)(\d*)$'
    match = re.search(pattern, log)
    if match:
        m = match.group()
    else:
        return log
    
    if m[0] == '.':
        print('DOT')
        return m[:5]
    
    if match.group(1):
        if int(match.group(1)) > 9999:
            return 'error'
    
    m = Decimal(m)
    m_r = round(m, 3)
    print(f'm_r = {m_r}')
    
    if int(m_r) > 9999:
        return 'error'
    
    log = re.sub(match.group(), str(m_r).lstrip('0'), log)
    print(log)
    log = log[:5]
    print(f'log after round_to_5_digits_float is {log}')
    
    return str(log)


def round_to_5_digits_sign_float(log):
    '''
    For float, beginning and trailing zeros should be removed (until the "." if possible): 0.1200 -> .12 , 123.00 -> 123. 
    It should be done after the rounding: 1.000123 -> 1. 
    Stripping of trailing zeros should only be done after entering a number has concluded (non-digit character pressed).
    
    assert calculator("0001.1000-") == "1.1"
    '''
    print(f'Starting round_to_5_digits_sign_float')
    pattern = r'^(\d*\.\d*)([\-\+\=]+)$'
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    number = match.group(1)
    sign = match.group(2)
    print(f'sign = {sign}')
    number = round_to_5_digits_float(number).rstrip('0')
    print(f'number1 = {number}')
    
    if number == 'error':
        return 'error'
    
    log = str(number) + sign
    
    # log = re.sub(match.group(), str(m_r) + match.group(4), log)
    print(f'log after round_to_5_digits_sign_float is {log}')
    
    return str(log)


def replace_number_and_minus_or_plus_before_equal_float(log):
    '''
    "+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself)
    assert calculator('999.999+=========') == 'error'
    2.4+= to be replaced with the result from 2.4 + 2.4 (so, with 4.8)
    '''
    print(f'Starting replace_number_and_minus_or_plus_before_equal_float')
    pattern = r'(\d*\.\d*)([\-\+])\='
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    my_float = match.group(1)
    print(f'my_float is {my_float}')
    op = match.group(2)
    print(f'op is {op}')
    
    if eval(my_float + op + my_float) < 9999:
        replacement = str(eval(my_float + op + my_float)) + op
    else:
        return 'error'
    
    print(f'replacement is {replacement}')
    
    log = re.sub(pattern, replacement, log, 1)
    print(f'log after replace_number_and_minus_or_plus_before_equal_float is {log}')
    
    log = round_to_5_digits_float(log)
    
    print(f'log after replace_number_and_minus_or_plus_before_equal_float and rounding is {log}')
    
    match = re.search(pattern, log)
    log = replace_number_and_minus_or_plus_before_equal_float(log)
    
    return str(log)
    
    
def replace_digits_and_minus_or_plus_before_equal(log):
    '''
    "+=" or "-=" - adding/subtracting the number (or operations result) 
    before the combination (doubling the number/subtracting itself)
    assert calculator('50000-====') == 'error'
    4+= to be replaced with the result from 4 + 4 (so, with 8)
    '''
    print(f'Starting replace_digits_and_minus_or_plus_before_equal')
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
    print(f'Starting repeating_the_last_operation')
    # The pattern has 3 groups: (digit) (operation) (==)
    #pattern = r'([\+\-\*\/]+)(\d*)(={2})'
    pattern = r'([\+\-\*\/]+)(\d*)(={2})'
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    print(f'The match before == is {match.group()}')
    op, digits, equals = match.group(1), match.group(2), match.group(3)
    log = log.replace(op + digits + equals, op + str(int(digits)*2) + '=') if int(digits)*2 < 99999 else 'error'
    print(f'log after replacing == with {op + digits + "="} is {log}')
    
    if '==' in log and 'error' not in log:
        repeating_the_last_operation(log)
    else:
        print(f'log after repeating_the_last_operation is {log}')
        return log


def repeating_the_last_operation_float(log):
    '''
    "==" means repeating the last operation
    '''
    print(f'Starting repeating_the_last_operation')
    # The pattern has 3 groups: (digit) (operation) (==)
    pattern = r'([\+\-\*\/]+)(\d*\.\d*)(={2})'
    match = re.search(pattern, log)
    
    if not match:
        return log
    
    print(f'The match before == is {match.group()}')
    op, digits, equals = match.group(1), match.group(2), match.group(3)
    log = log.replace(op + digits + equals, op + str(int(digits)*2) + '=') if int(digits)*2 < 99999 else 'error'
    print(f'log after replacing == with {op + digits + "="} is {log}')
    
    if '==' in log and 'error' not in log:
        repeating_the_last_operation_float(log)
    else:
        print(f'log after repeating_the_last_operation is {log}')
        return log
    

def replace_signs_with_last(log):
    '''
    among +- signs between numbers, the last one should be taken;
    '''
    print(f'Starting replace_signs_with_last')
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
    print(f'Starting replace_equal_and_signs_at_end')
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


def replace_digits_sign_digits_equal_digits(log):
    '''
    2+3=7+7=
    '''
    print(f'Starting replace_digits_sign_digits_equal_digits')
    pattern = r'(\d+[\-\+]+\d+=)(\d+)'
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        log = log.replace(match.group(), match.group(2))
        #log = log.replace(match.group(), str(eval(match.group()[:-1]+)))
        print(f'log after replace_digits_sign_digits_equal_digits is {log}')
        return log


def replace_digits_sign_digits_equal_or_sign(log):
    '''
    1+2=
    Check, also, maybe after = is another = 
    '''
    print(f'Starting replace_digits_sign_digits_equal_or_sign')
    #pattern = r'([\-\+]*\d+[\-\+]+\d+[=\-\+])'
    pattern = r'([\-\+]*\d+[\-\+]+\d+)([=\-\+])'
    match = re.search(pattern, log)
    pattern_equals = r'(\d+[\-\+]+\d+==)'
    match_equals = re.search(pattern_equals, log)
    
    if (not match) or (match_equals):
        #print(f'(not match) or (match_equals)')
        return log
    
    print(f'match in replace_digits_sign_digits_equal_or_sign is {match.group()}')
    
    if abs(eval(match.group()[:-1])) > 99999:
        return 'error'
    
    log = log.replace(match.group(), str(eval(match.group(1))) + str(match.group(2)))
    
    match = re.search(pattern, log)
    
    if match:
        log = replace_digits_sign_digits_equal_or_sign(log)
    else:
        print(f'log after replace_digits_sign_digits_equal_or_sign is {log}')
    
    return log


def replace_digits_sign_digits_sign_equal_at_start(log):
    '''
    3+2-=
    '''
    print(f'Starting replace_digits_sign_digits_sign_equal_at_start')
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
    print(f'Starting find_last_plus_or_minus')
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
    

def replace_equal_and_signs_at_beginning_OLD(log):
    print(f'Starting replace_equal_and_signs_at_beginning')
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
    print(f'log after replace_equal_and_signs_at_beginning is {log}')
    return log


def replace_equal_and_signs_at_beginning(log):
    print(f'Starting replace_equal_and_signs_at_beginning')
    pattern = r'\d'
    first_digit = re.search(pattern, log)
    
    if not first_digit:
        return log
    
    pos = first_digit.start()
    
    string_before_digit = log[:pos]
    last_sign = find_last_plus_or_minus(string_before_digit)
    print(last_sign)
    
    if last_sign == None:
        return log[pos:]
    
    if last_sign[0] == '+':
        last_sign = last_sign[1:]
        
    # replace string_before_digit with last_sign
    log = log.replace(string_before_digit, last_sign, 1)    
    print(f'log after replace_equal_and_signs_at_beginning is {log}')
    return log
    

def replace_sign_or_equal_and_digit_at_end(log):
    print(f'Starting replace_sign_or_equal_and_digit_at_end')
    pattern = r'[\+\-=](\d+)$'
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        pos = match.start()
        print(f'log after replace_sign_or_equal_and_digit_at_end is {log[pos+1:]}')
        return log[pos+1:]
    

def replace_digits_equal_sign_digits(log):
    print(f'Starting replace_digits_equal_sign_digits')
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
    
    
def replace_digits_and_sign_at_end(log):
    print(f'Starting replace_digits_and_sign_at_end')
    #print(f'log before replace_digit_and_sign_at_end is {log}')
    pattern = r'(\d+)[\+\-=]$'
    match = re.search(pattern, log)
    if match == None:
        return log
    else:
        log = log.replace(match.group(), match.group(1))
        print(f'log after replace_digit_and_sign_at_end is {log}')
        return log
    
    
def delete_zeros_after_dot(log):
    print(f'Starting delete_zeros_after_dot')
    pattern = r'(\d+\.)(0*)$'
    match = re.search(pattern, log)
    if match == None:
        return log
    elif len(match.group()) > 5:
        log = log.replace(match.group(), match.group(1))
        print(f'log after delete_zeros_after_dot is {log}')
        return log
    
    return log
    
    

#@timer    
def calculator(log: str) -> str:
    print(f'------The starting log is {log}')
    
    log = left_strip_zeros(log)
    log = replace_equal_and_signs_at_beginning(log)
    log = truncate_digits(log)
    log = round_to_5_digits(log)
    log = round_to_5_digits_float(log)
    log = round_to_5_digits_sign_float(log)
    log = replace_number_and_minus_or_plus_before_equal_float(log)
    log = replace_digits_equal_sign_digits(log)
    log = replace_digits_sign_digits_sign_equal_at_start(log)
    log = replace_digits_and_minus_or_plus_before_equal(log)
    log = repeating_the_last_operation(log)
    repeating_the_last_operation_float(log)
    log = replace_signs_with_last(log)
    log = replace_equal_and_signs_at_end(log)
    log = replace_sign_or_equal_and_digit_at_end(log)
    log = replace_digits_sign_digits_equal_digits(log)
    log = replace_digits_sign_digits_equal_or_sign(log)
    log = replace_digits_and_sign_at_end(log)
    log = delete_zeros_after_dot(log)
    
    print(f'New log after 15 replacements: {log}') 
    
    if log in ['+', '-', '=', '']:
        return '0'
    
    if log == 'error' or (type(log) == int and abs(int(log)) > 99999):
        return 'error'
    
    try:
        float(log) or int(log)
        return log
    except ValueError:
        print(f'log is not float or int')
    
    
print("Example:")
assert calculator('100000') == '10000'


# These "asserts" are used for self-checking
print(f'---1.---')
assert calculator("0001.1000") == "1.100"
print(f'---2.---')
assert calculator("0001.1000-") == "1.1"
print(f'---3.---')
assert calculator("999.9999999+=") == "2000."
print(f'---4.---')
assert calculator("1.000123") == "1.000"
print(f'---5.---')
assert calculator("9999.9999999+=") == "error"
print(f'---6.---')
assert calculator("90000+10000=") == "error"
print(f'---7.---')
assert calculator("90000+10000-10000=") == "error"
print(f'---8.---')
assert calculator("90000+10000-10000") == "10000"
print(f'---9.---')
assert calculator("123456789") == "12345"
print(f'---10.---')
assert calculator("123456789+5=") == "12350"
print(f'---11.---')
assert calculator("5+123456789") == "12345"
print(f'---12.---')
assert calculator("50000+=") == "error"
print(f'---13.---')
assert calculator("3+=") == "6"
print(f'---14.---')
assert calculator("3+2==") == "7"
print(f'---15.---')
assert calculator("4-1==") == "2"
print(f'---16.---')
assert calculator("3+-2=") == "1"
print(f'---17.---')
assert calculator("-=-+3-++--+-2=-") == "1"
print(f'---18.---')
assert calculator("000000") == "0"
print(f'---19.---')
assert calculator("0000123") == "123"
print(f'---20.---')
assert calculator("12") == "12"
print(f'---21.---')
assert calculator("+12") == "12"
print(f'---22.---')
assert calculator("") == "0"
print(f'---23.---')
assert calculator("1+2") == "2"
print(f'---24.---')
assert calculator("2+") == "2"
print(f'---25.---')
assert calculator("1+2=") == "3"
print(f'---26.---')
assert calculator("1+2-") == "3"
print(f'---27.---')
assert calculator("1+2=2") == "2"
print(f'---28.---')
assert calculator("=5=10=15") == "15"
print(f'---29.---')
assert calculator('50000-====') == 'error'
print(f'---30.---')
assert calculator('5+7=') == '12'
print(f'---31.---')
assert calculator('2+3=+7=') == '12'
print(f'---32.---')
assert calculator('000005+003') == '3'
print(f'---33.---')
assert calculator('-5-10+15-') == '0'
print(f'---34.---')
assert calculator('+1+2+3+4=') == '10'
print(f'---35.---')
assert calculator('+') == '0'
print(f'---36.---')
assert calculator('0001.2005+=-1+10.43+99979') == '99979'
print(f'---37.---')
assert calculator('-+++--+.12009') == '.1200'
print(f'---38.---')
assert calculator('999.999+=========') == 'error'
print(f'---39.---')
assert calculator('100000') == '10000'

print("The mission is done! Click 'Check Solution' to earn rewards!")