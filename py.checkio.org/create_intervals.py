'https://py.checkio.org/en/mission/create-intervals/'

'''
From a set of ints you have to create a list of closed intervals as tuples, so the intervals are covering all the values found in the set.

Input: A set of ints.

Output: A list of tuples of two ints, indicating the endpoints of the interval. The Array should be sorted by start point of each interval
'''

def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
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



# Best Solution: https://py.checkio.org/mission/create-intervals/publications/Lemmi/python-3/lefts-and-rights-separately/?ordering=most_voted&filtering=all
def create_intervals(data):
    left = [x for x in data if x - 1 not in data]
    right = [x for x in data if x + 1 not in data]
    return list(zip(sorted(left), sorted(right)))



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')