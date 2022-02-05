'https://py.checkio.org/en/mission/merge-intervals/'

'''
You are given a sequence of intervals, as tuples of ints where the tuples are sorted by their first element in ascending order.
It is your task to minimize the number of intervals by merging those that intersect or by removing intervals fitting into another one.

Since the range of values for the intervals is restricted to integers, you must also merge those intervals between which no value can be found.
'''

def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """
    result = [intervals[0]]
    print(result)
    for item in intervals:
        print(f'item = {item}')
        if item[0] <= result[-1][1] or (item[0] - result[-1][1]) == 1:
            if item[1] >= result[-1][1]:
                new_interval = (result[-1][0], item[1])
                print(new_interval)
            else:
                new_interval = (result[-1][0], result[-1][1])
                print(new_interval)
            result.pop()
            result.append(new_interval)
            print(result)
        else:
            result.append(item)    
            print(result)
        
    print(result)
    return result


# Best solution
# https://py.checkio.org/mission/merge-intervals/publications/StefanPochmann/python-3/simple/share/6d06f29be8380889fdc41418ad155755/
def merge_intervals(intervals):
    result = []
    for interval in intervals:
        if not result or interval[0] > result[-1][1] + 1:
            result.append(interval)
        result[-1] = result[-1][0], max(result[-1][1], interval[1])
    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')