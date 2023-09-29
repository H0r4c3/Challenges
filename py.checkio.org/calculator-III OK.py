'https://py.checkio.org/en/mission/calculator-iii/'

'''
Expected behavior:

beginning zeros should be removed, only-zeros number - converted to single zero;
among +- signs between numbers, the last one should be taken;
"==" means repeating the last operation;
"+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself);
the calculator ignores digit you enter after 5th;
"-" for numbers < 0 is NOT taking digit place;
if the abs(result) is more than 99999 - "error" is shown as a result.
'''

def calculator(log: str) -> str:
    second, screen, new, op, magic = 0, 0, True, '=', lambda: (screen, -screen)[op == '-']

    print(f'log = {log}')

    for key in log:
        print(f'key = {key}')
        if key.isdigit():
            screen = screen * 10 * (not new) + int(key)
            print(f'screen = {screen}')
        elif key in '+-':
            second = screen = screen if op == '=' or new else second + magic()
            print(f'second = {second}')
        elif key == '=' == op:
            screen = screen + second
            print(f'screen = {screen}')
        elif key == '=':
            screen = (second, screen)[new] + (second := magic())
            print(f'screen = {screen}')
            
        op = (op, key)[new := key in '+-=']
        print(f'op = {op}')

    print(f'str(screen) = {str(screen)}')
    return str(screen)


#print("Example:")
#print(calculator("100000"))

# These "asserts" are used for self-checking
print(f'---1.---')
assert calculator("90000+10000=") == "error"
print(f'---2.---')
assert calculator("90000+10000-10000=") == "error"
print(f'---3.---')
assert calculator("90000+10000-10000") == "10000"
print(f'---4.---')
assert calculator("123456789") == "12345"
print(f'---5.---')
assert calculator("123456789+5=") == "12350"
print(f'---6.---')
assert calculator("5+123456789") == "12345"
print(f'---7.---')
assert calculator("50000+=") == "error"
print(f'---8.---')
assert calculator("3+=") == "6"
print(f'---9.---')
assert calculator("3+2==") == "7"
print(f'---10.---')
assert calculator("4-1==") == "2"
print(f'---11.---')
assert calculator("3+-2=") == "1"
print(f'---12.---')
assert calculator("-=-+3-++--+-2=-") == "1"
print(f'---13.---')
assert calculator("000000") == "0"
print(f'---14.---')
assert calculator("0000123") == "123"
print(f'---15.---')
assert calculator("12") == "12"
print(f'---16.---')
assert calculator("+12") == "12"
print(f'---17.---')
assert calculator("") == "0"
print(f'---18.---')
assert calculator("1+2") == "2"
print(f'---19.---')
assert calculator("2+") == "2"
print(f'---20.---')
assert calculator("1+2=") == "3"
print(f'---21.---')
assert calculator("1+2-") == "3"
print(f'---22.---')
assert calculator("1+2=2") == "2"
print(f'---23.---')
assert calculator("=5=10=15") == "15"

print("The mission is done! Click 'Check Solution' to earn rewards!")