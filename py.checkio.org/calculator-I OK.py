'https://py.checkio.org/en/mission/calculator-i/share/4ff956f3a5c3347af572c0a57046ae7a/'

'''
In the first mission only digits and single signs (only +, -, =) between them are used.

Expected behavior:

beginning operations are ignored;
beginning zeros should be removed, only-zeros number - converted to single zero.
'''

TESTS = [{
            "input": ["000000"],
            "answer": "0",
            "explanation": "single zero instead of multi-zeros number",
        },
        {
            "input": ["0000123"],
            "answer": "123",
            "explanation": "remove beginning zeros",
        },
        {
            "input": ["12"],
            "answer": "12",
            "explanation": "you see what you enter",
        },
        {
            "input": ["+12"],
            "answer": "12",
            "explanation": "ignore beginning operations",
        },
        {
            "input": [""],
            "answer": "0",
            "explanation": "when power on - 0 on the screen",
        },
        {
            "input": ["1+2"],
            "answer": "2",
            "explanation": "last entered number, no operations after",
        },
        {
            "input": ["2+"],
            "answer": "2",
            "explanation": "single +/- do nothing",
        },
        {
            "input": ["1+2="],
            "answer": "3",
            "explanation": "standard operation",
        },
        {
            "input": ["1+2-"],
            "answer": "3",
            "explanation": "last sign requires previous calculations to be done",
        },
        {
            "input": ["1+2=2"],
            "answer": "2",
            "explanation": "entering number rewrites previous result",
        },
        {
            "input": ["=5=10=15"],
            "answer": "15",
        },
        {
            "input": ["000005+003"],
            "answer": "3",
        },
        {
            "input": ["000005+003="],
            "answer": "8",
        },
        {
            "input": ["-5-10+15"],
            "answer": "15",
        },
        {
            "input": ["-5-10+15-"],
            "answer": "10",
        },
        {
            "input": ["+1+2+3+4="],
            "answer": "10",
        },
        {
            "input": ["+"],
            "answer": "0",
        }]

# My Solution:

import re

def left_strip_zeros_and_plus(log):
    new_log = log
    for char in log:
        if char in ['0', '+']:
            new_log = log.lstrip(char)
        else:
            break
        
    if new_log in ('+', '-', '*', '/', ''):
        return '0'
    
    return new_log
    

def calculator(log: str) -> str:
    print(f'log = {log}')
    
    log = left_strip_zeros_and_plus(log)
    
    if log[-1] not in ('=', '+', '-', '*', '/'):
        try:
            log = re.search(r'[1-9]+$', log).group()
        except AttributeError:
            return '0'
    else:
        log = re.sub(r'[0]+([1-9]+)', r'\1', log)
        log = str(eval(log[:-1]))
    
    result = log
    print(f'result = {result}')
    
    return log if log else '0'
    
    

# Best Solution:
# https://py.checkio.org/mission/calculator-i/publications/Sim0000/python-3/eval/#comments

def calculator_(log: str) -> str:
    screen = last = left = op = ''
    for c in log:
        if c.isdigit():
            if not last.isdigit() or screen == '0': screen = '' # clear screen
            screen += c
        elif screen: # operator (when screen == '', c is leading operator)
            if left: screen = str(eval(left + op + screen))
            left, op = (screen, c) if c != '=' else ('', '')
        last = c
    return screen or '0'


# Best Solution:
# https://py.checkio.org/mission/calculator-i/publications/CDG.Axel/python-3/8-lines-proc/

def calculator_(log: str) -> str:
    prev, current, save, operation = 0, 0, False, '='
    
    for key in log:
        if key.isdigit():
            current = current * 10 * save + int(key)
            save = True
        elif key in '+-=':
            prev = current = prev + current if operation == '+' else prev - current if operation == '-' else current
            operation, save = key, False

    return str(current)


# Best Solution: 
# https://py.checkio.org/mission/calculator-i/publications/Magu/python-3/first/?ordering=most_voted&filtering=all

import re

def calculator_(log: str) -> str:
    
    if log in ('+', '-', '*', '/') or not log:
        return '0'
    
    if not log[-1] in ('=', '+', '-', '*', '/'):
        try:
            log = re.search(r'[0]*[1-9]+$', log).group().lstrip('0')
        
        except AttributeError:
            return '0'
        
    else:
        log = re.sub(r'[0]+([1-9]+)', r'\1', log)
        log = str(eval(log[:-1]))
    
    return log if log else '0'



print("Example:")
#print(calculator("1+2"))

# These "asserts" are used for self-checking
print(f'---1.---')
assert calculator("000000") == "0"
print(f'---2.---')
assert calculator("0000123") == "123"
print(f'---3.---')
assert calculator("1313") == "1313"
print(f'---4.---')
assert calculator("+13") == "13"
print(f'---5.---')
assert calculator("") == "0"
print(f'---6.---')
assert calculator("1+3") == "3"
print(f'---7.---')
assert calculator("4+") == "4"
print(f'---8.---')
assert calculator("1+4=") == "5"
print(f'---9.---')
assert calculator("1+5-") == "6"
print(f'---10.---')
assert calculator("1+6=7") == "7"
print(f'---11.---')
assert calculator("=5=10=15") == "15"
print(f'---12.---')
assert calculator('000005+008') == '8'
print(f'---13.---')
assert calculator('000005+003=') == '8'
print(f'---14.---')
assert calculator('-5-10+15-') == '0'
print(f'---15.---')
assert calculator('+') == '0'

print("The mission is done! Click 'Check Solution' to earn rewards!")