'https://py.checkio.org/en/mission/nearest-value/'

'''
Find the nearest value to the given one.

You are given a list of values as set form and a value for which you need to find the nearest one.
'''

def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    
    values_list = sorted(list(values))
    
    index_list = [(values_list.index(item), abs(item - one)) for item in values_list]
    index_list.sort(key=lambda x: x[1])
    index_ok = index_list[0][0]
    
    return values_list[index_ok]


# Best solution: https://py.checkio.org/mission/nearest-value/publications/mortonfox/python-3/first/?ordering=most_voted&filtering=all
def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))


if __name__ == '__main__':
    print(nearest_value({4, 7, 10, 11, 12, 17}, 8))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1