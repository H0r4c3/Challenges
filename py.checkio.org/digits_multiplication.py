'https://py.checkio.org/en/mission/digits-multiplication/'

'''
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.
'''

def checkio(number: int) -> int:
    result = 1
    my_string = str(number)
    for item in my_string:
        if int(item) != 0:
            result = result * int(item)

    return result


if __name__ == '__main__':
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1