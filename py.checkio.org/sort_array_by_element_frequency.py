'https://py.checkio.org/en/mission/sort-array-by-element-frequency/'

'''
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable

Output: Iterable
'''

from itertools import repeat

def frequency_sort(items):
    
    my_dict = dict()
    my_list = list()
    
    for item in items:
        count = items.count(item)
        my_dict[item] = count
    
    sorted_list = sorted(my_dict.items(), key = lambda x : x[1], reverse=True)
    
    sorted_dict = dict(sorted_list)
    
    my_list = [x for item in sorted_dict for x in repeat(item, my_dict[item])]
        
    return my_list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) # -> 4,4,4,4,2,2,2,6,6

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]