'https://py.checkio.org/en/mission/group-equal-consecutive/'

'''
Given a list of elements, create and return a list whose elements are lists that contain the consecutive runs of equal elements of the original list. 
Note that elements that aren’t duplicated in the original list should become singleton lists in the result, 
so that every element gets included in the resulting list of lists.
'''
from itertools import groupby

def group_equal(els):
    new_list = [list(group) for _, group in groupby(els)]
    print(new_list)
    
    return new_list


if __name__ == '__main__':
    print("Example:")
    #print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")