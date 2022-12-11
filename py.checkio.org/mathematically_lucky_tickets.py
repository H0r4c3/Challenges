'https://py.checkio.org/en/mission/mathematically-lucky-tickets/'

'''
Task: Given a 6-digit number of the ticket, the program should determine whether it is mathematically lucky or not.

Input: 6 digits as a string.

Output: Is it mathematically lucky or not as a boolean.
'''

def checkio(data):

    #replace this for solution
    return True or False


# Best Solution: 
# https://py.checkio.org/mission/mathematically-lucky-tickets/publications/David_Jones/python-3/recursion/share/0ad55613f33a362f71e6e1e656a6e59b/

from itertools import product

def possible_results(data):
    yield int(data)
    for i in range(1, len(data)):
        for (x,y) in product(
            possible_results(data[:i]), possible_results(data[i:])
        ):
            yield from (x+y, x-y, x*y)
            if y:
                yield x/y

def checkio(data):
    return all(result != 100 for result in possible_results(data))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
    print('Done!!!')