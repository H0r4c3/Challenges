'https://py.checkio.org/en/mission/aggregate-and-count/'

'''
You have a list of values where each element is a list of two values. First is a name and the second one is counter.

What you need to do is to aggregate those values into a dict, which is easy, you can simply use function disc for that. 
But, name is not unique, so if you find more that one elements with the same name, you should sum their counters in the aggregated dict.
'''

# My first Solution:
def aggregate_and_count_(items:list) -> dict:
    result = {}
    keys = list()
    
    for i in range(len(items)):
        k = items[i][0]
        v = items[i][1]
        
        if k not in keys:
            result[k] = v
            keys.append(k)
        else:
            result[k] += v
    
    print(result)
    return result


# My second Solution
def aggregate_and_count_(items:list) -> dict:
    result = {}
    
    for i in range(len(items)):
        k = items[i][0]
        v = items[i][1]
        
        if k not in result:
            result[k] = v
        else:
            result[k] += v
    
    print(result)
    return result


# My third Solution
def aggregate_and_count(items:list) -> dict:
    result = {}
    
    # for item in items:
    #     key = item[0]
    #     value = item[1]
    
    for key, value in items:
        
        if key not in result:
            result[key] = value
        else:
            result[key] += value
    
    print(result)
    return result


# Best Solution: 
# https://py.checkio.org/mission/aggregate-and-count/publications/veky/python-3/dicountiary/?ordering=most_voted&filtering=all

import collections

def aggregate_and_count(items: list) -> dict:
    result = collections.Counter()
    print(result)
    
    for item, frequency in items: 
        result[item] += frequency
    
    return result





print('Example:')
print(aggregate_and_count([['a', 1], ['b', 2], ['c', 3], ['a', 5]]))

assert aggregate_and_count([['a', 1], ['b', 2]]) == {'a': 1, 'b': 2}
assert aggregate_and_count([['a', 1], ['a', 2]]) == {'a': 3}
assert aggregate_and_count([['a', 1], ['b', 2], ['c', 3], ['a', 5]]) == {'a': 6, 'b': 2, 'c': 3}
assert aggregate_and_count([['a', 1]]) == {'a': 1}

print("The aggregation is done! Click 'Check' to earn cool rewards!")