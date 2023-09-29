'https://py.checkio.org/en/mission/calculator-ii/share/8bf6e28b9dfe841548135283262159b9/'

'''
Expected behavior:

beginning zeros should be removed, only-zeros number - converted to single zero;
among +- signs between numbers, the last one should be taken;
"==" means repeating the last operation;
"+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself).
'''

import re
 
def strip_zeros_from_digits(log):
    log_split = re.split(r'(\D)', log) # split after non-numeric chars
    log_split_strip = [item.lstrip('0') for item in log_split]
    new_log = ''.join(log_split_strip)
    print(f'new_log after strip_zeros_from_digits = {new_log}')
    
    return new_log

def replace_operation_with_result(log):
    
    # assert calculator('3+2==') == '7' 
    operation2 = re.search('^\d+[+\-*/]\d+={2}', log)
    print(f'operation2 found in log = {operation2}')
    if operation2:
        operation2 = operation2.group()
        print(f'operation2 = {operation2}')
        oper = re.search('[+\-*/]', operation2).group()
        second_d = re.findall('\d+', operation2)[1]
        print(f'oper = {oper}')
        print(f'second_d = {second_d}')
        result = operation2[:-2] + str(oper) + str(second_d)
        result = str(eval(result))
        print(f'result for replacing operation = {result}')

        new_log = log.replace(operation2, result)
        print(f'new_log after replace_operation_with_result = {new_log}')
        return new_log
    
    
    # 5+6=1
    operation3 = re.search('^\d+[+\-*/]\d+=\d+', log)
    print(f'operation3 found in log = {operation3}')
    if operation3:
        operation3 = operation3.group()
        print(f'operation3 = {operation3}')
        third_d = re.search('=\d+', operation3).group()
        print(f'third_d = {third_d}')
        new_log = log.replace(operation3, third_d[1:])
        return new_log
    
    
    # 5+6=
    operation1 = re.search('^\d+[+\-*/]\d+=', log)
    print(f'operation1 found in log = {operation1}')    
    if operation1:
        operation1 = operation1.group()
        result = str(eval(operation1[:-1]))
        print(f'result for replacing operation = {result}')

        new_log = log.replace(operation1, result)
        print(f'new_log after replace_operation_with_result = {new_log}')
        return new_log
    
    return log
    
    
def calculator(log: str) -> str:
    log = strip_zeros_from_digits(log)
    if log.isnumeric():
        return log
    
    # assert calculator("3+2==") == "7"
    # assert calculator("4-1==") == "2"
    log = replace_operation_with_result(log)
    if log.isnumeric():
        return log
    
    e = log.rfind('=') # index of last '='
    p = log.rfind('+') # index of last '+'
    m = log.rfind('-') # index of last '-'
    last = max(e, p, m)
    last_op = max(p, m)
    
    chars_between_numbers = re.findall(r'(?<=\d)[^\d]+(?=\d)', log)
    #print(f'chars_between_numbers = {chars_between_numbers}')
    
    numbers = re.findall(r'\d+', log)
    #print(f'numbers = {numbers}')
    
    numbers_with_signs = re.findall(r'[+-]?\d+', log)
    #print(f'numbers_with_signs = {numbers_with_signs}')
    
    idx_of_equal = log.find('=') # first index of = sign
    
    if log.count('=') > 1 and (e-idx_of_equal != 1):
        return calculator(log[idx_of_equal+1 : ])
    
    # assert calculator("000000") == "0"
    if (not log.isnumeric() and len(log) == 1) or log.count('0') == len(log):
        print(f'0. Result = 0')
        return '0'
    
    # assert calculator("3+=") == "6"
    # +=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself).
    elif log[-1] == '=' and log[-2] == '+':
        print(f'1. Result = {str(int(log[:-2]) + int(log[:-2]))}')
        return str(int(log[:-2]) + int(log[:-2]))
    
    #assert calculator('78-=') == '0'
    # +=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself).
    elif log[-1] == '=' and log[-2] == '-':
        print(f'1b. Result = {"0"}')
        return "0"
    
    # assert calculator("-=-+3-++--+-2=-") == "1"
    # assert calculator('+-=12=') == '12'
    # assert calculator('2+3=7+7=') == '14'
    if  log[-1] == '+' or log[-1] == '-' or log[-1] == '=':
            numbers_with_signs = ''.join(numbers_with_signs)
            print(f'3a. Result = {str(eval(numbers_with_signs))}')
            return str(eval(numbers_with_signs))
    
    # assert calculator("+12") == "12"
    elif (log.startswith('+') or log.startswith('-')) and log[1:].isnumeric():
        print(f'4a. New log = {log[1:]}')
        return calculator(log[1:])
    
    # assert calculator("1+2") == "2"
    elif (last == p or last == m) and last != len(log)-1:
        print(f'4b. New log = {log[last+1:]}')
        return calculator(log[last+1:])
    
    #assert calculator("1+2=2") == "2"
    elif last == e and log[e+1:].isnumeric():
        print(f'5. Result = {log[e+1:]}')
        return log[e+1:]
        
    # assert calculator('2+3=+7=') == '12'
    elif re.search('^\d+[+\-*/]\d+=', log):
        operation = re.search('^\d+[+\-*/]\d+=')
        log = re.sub(operation, eval(operation), log)
        print(f'new log = {log}')
        return calculator(log)
        
    return ""


# Best Solution: 
# https://py.checkio.org/mission/calculator-ii/publications/CDG.Axel/python-3/could-12-lines-proc-be-clear/?ordering=most_voted&filtering=all

def calculator(log: str) -> str:
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

print("The mission is done! Click 'Check Solution' to earn rewards!")