'https://py.checkio.org/en/mission/replace-last/'

'''
In a given list the last element should become the first one. 
An empty list or list with only one element should stay the same
'''

def replace_last(line: list) -> list:
    if line == []:
        return []
    
    if len(line) == 1:
        return line
    
    else:
        line1 = line[-1 : ] + line[0 : -1]
        return line1


if __name__ == '__main__':
    print("Example:")
    print(replace_last([2, 3, 4, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []