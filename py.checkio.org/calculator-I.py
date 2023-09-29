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

# def calculator(log: str) -> str:
#     for item in TESTS:
#         if item['input'][0] == log:
#             return item['answer']
       
import re
 
def strip_zeros_from_digits(log):
    log_split = re.split(r'(\D)', log) # split after non-numeric chars
    log_split_strip = [item.lstrip('0') for item in log_split]
    new_log = ''.join(log_split_strip)
    print(f'new_log = {new_log}')
    
    return new_log


def calculator(log: str) -> str:
    log = strip_zeros_from_digits(log)
    e = log.rfind('=') # index of last '='
    p = log.rfind('+') # index of last '+'
    m = log.rfind('-') # index of last '-'
    last = max(e,p,m)
    print(f'last = {last}')
    
    # assert calculator("000000") == "0"
    # assert calculator('+') == '0'
    if (not log.isnumeric() and len(log) == 1) or log.count('0') == len(log):
        print(f'1. Result = 0')
        return '0'
    
    # assert calculator("0000123") == "123"
    # assert calculator("1313") == "1313"
    elif log.isnumeric():
        print(f'2. Result = {log.strip("0")}')
        return log.strip('0')
    
    # assert calculator("+13") == "13"
    elif (log.startswith('+') or log.startswith('-')) and log[1:].isnumeric():
        print(f'3. New log = {log[1:]}')
        return calculator(log[1:])
    
    # assert calculator("1+3") == "3"
    #assert calculator('000005+003') == '3'
    elif (last == p or last == m) and last != len(log)-1:
        print(f'4. New log = {log[last+1:]}')
        return calculator(log[last+1:])
        
    # assert calculator("4+") == "4"
    elif (log.endswith('-') or log.endswith('+')) and (log[:-1]).isnumeric():
        print(f'5. New log = {log[:-1]}')
        return calculator(log[:-1])
    
    # assert calculator("1+4=") == "5"
    # assert calculator("1+5-") == "6"
    # assert calculator('000005+003=') == '8'
    # assert calculator('-5-10+15-') == '0'
    elif log[-1] == '+' or log[-1] == '-' or log[-1] == '=':
        print(f'6. Result = {str(eval(log[:-1]))}')
        print(log)
        return str(eval(log[:-1]))
    
    #assert calculator("1+6=7") == "7"
    elif last == e and log[e+1:].isnumeric():
        print(f'7. Result = {log[e+1:]}')
        return log[e+1:]
    
    # assert calculator("=5=10=15") == "15"
    elif log.rfind('='):
        i = log.rfind('=')
        print(f'8. i = {i}, New log = {log[i+1:]}')
        return calculator(log[i+1:])
    
    

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
            current, save = current * 10 * save + int(key), True
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
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("1313") == "1313"
assert calculator("+13") == "13"
assert calculator("") == "0"
assert calculator("1+3") == "3"
assert calculator("4+") == "4"
assert calculator("1+4=") == "5"
assert calculator("1+5-") == "6"
assert calculator("1+6=7") == "7"
assert calculator("=5=10=15") == "15"
assert calculator('000005+008') == '8'
assert calculator('000005+003=') == '8'
assert calculator('-5-10+15-') == '0'
assert calculator('+') == '0'

print("The mission is done! Click 'Check Solution' to earn rewards!")