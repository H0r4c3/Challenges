'https://py.checkio.org/en/mission/sum-numbers/'

'''
In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.
'''

def sum_numbers(text: str) -> int:
    result = 0
    text_list = text.split()
    for item in text_list:
        if item.isdigit():
            result = result + int(item)
    
    return result


import re

def sum_numbers_regex(text: str) -> int:
    r = re.compile('^\d+|[^\w]\d+[^\w]|\d+$')
    digits = re.findall(r, text)
    result = sum(map(int, digits))
    
    return result


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers_regex('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0