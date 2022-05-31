'https://py.checkio.org/en/mission/beginning-zeros/'

'''
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.
'''

def beginning_zeros_(number: str) -> int:
    new_number = number.lstrip('0')
    result = len(number) - len(new_number)
    
    return result


# Another solution
# https://py.checkio.org/mission/beginning-zeros/publications/oduvan/python-3/first/

def beginning_zeros(number: str) -> int:
    str_int = str(int(number))
    
    print(str_int == '0')
    return len(number) - len(str_int) + (str_int == '0')


if __name__ == '__main__':
    
    #print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print('Done!!!')