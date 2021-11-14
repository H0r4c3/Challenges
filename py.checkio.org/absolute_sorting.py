'https://py.checkio.org/en/mission/absolute-sorting/'

'''
The array (a list) has various numbers. You should sort it, but sort it by absolute value in ascending order. 
For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20). Your function should return the sorted list or tuple.
'''

def checkio(values: list) -> list:
    values_sorted = sorted(values, key=lambda x : abs(x))
    return values_sorted


if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]