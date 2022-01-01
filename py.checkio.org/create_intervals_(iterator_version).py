'https://py.checkio.org/en/mission/create-intervals-iterator-version/'

'''
From a set of ints (which will be an iterator of the sorted list) you have to create a list of closed intervals as tuples, so 
the intervals are covering all the values found in the set. After that you have to create an iterator object which is linked to this list.

A closed interval includes its endpoints! The interval 1..5 , for example, includes each value x that satisfies the condition 1 <= x <= 5 .

Values can only be in the same interval if the difference between a value and the next smaller value in the set equals one, otherwise a new interval begins. 
Of course, the start value of an interval is excluded from this rule.
A single value, that doesn’t fit into an existing interval becomes the start- and endpoint of a new interval.

Input: An iterator of the sorted list of ints.

Output: An iterator object linked to the list of tuples.
'''

def create_intervals_NOK(data):
    """
        Create a list of intervals out of set of ints.
    """
    result = list()
    
    next1 = next(data)
    start = next1
    next2 = next(data)
    end = next2
    
    while True:
        if next2 - next1 > 1:
            result.append((start, end))
            start = next2
            try:
                next1 = next(data)
                end = next1
            except StopIteration:
                result.append((start, start))
                print(result)
                return iter(result)
            try:
                next2 = next(data)
            except StopIteration:
                result.append((start, end))           
        else:
            try:
                next1 = next2
                end = next2
                next2 = next(data)
            except StopIteration:
                result.append((start, end))
                print(result)
                return iter(result)
            
import numpy as np
def create_intervals_NOK(data):
    """
        Create a list of intervals out of set of ints.
    """
    result = list()
    data_arr = np.array(list(data))
    diff_data = np.diff(data_arr)
    indexes = list(np.where(diff_data > 1)[0])
    print(list(diff_data))
    print(indexes)
    result = [(data_arr[0], data_arr[indexes[0]])]
    
    for item in indexes[1:]:
        result.append((data_arr[item-1], data_arr[item]))
        
    if data_arr[item] != data_arr[-1]:
        result.append((data_arr[item+1], data_arr[-1]))
        
    print(result)
    
    return iter(result)


# https://py.checkio.org/mission/create-intervals/publications/Kajin/python-3/first/share/34d3e7e235fe88f574564d47960e7bb5/
def create_intervals(data):
    data=list(data)
    data.sort()
    result = []
    if len(data) == 1:
        result.append((data[0],data[0]))
    elif len(data) > 1:
        start = data[0]
        stop = data[0]
        for index in range(len(data)):
            if start - data[index] == 1:
                start = data[index]
            elif data[index] - stop == 1:
                stop = data[index]            
            elif start -data[index] > 1 or data[index] - stop > 1:
                result.append((start, stop))
                start = stop = data[index]              
        result.append((start, stop))
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    res = create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))
    #res = create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))
    assert hasattr(res, '__iter__'), "your function should return the iterator object"
    assert hasattr(res, '__next__'), "your function should return the iterator object"

    assert list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [(1, 5), (7, 8), (12, 12)], "First"
    assert list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [(1, 8)], "Second"
    assert list(create_intervals(iter(sorted(list({1, 3, 7}))))) == [(1, 1), (3, 3), (7, 7)], "Third"
    print('Almost done! The only thing left to do is to Check it!')