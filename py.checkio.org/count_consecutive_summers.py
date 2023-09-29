'https://py.checkio.org/en/mission/count-consecutive-summers/'

'''
Positive integers can be expressed as sums of consecutive positive integers in various ways. 
For example, 42 can be expressed as such a sum in four different ways:(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42. 
As the last solution (d) shows, any positive integer can always be trivially expressed as a singleton sum that consists of that integer alone.

Compute how many different ways it can be expressed as a sum of consecutive positive integers.
'''

# My Solution = Using brute force (need to be optimized!!!)

from itertools import tee, islice

def grouping(iterable, n):
    '''
    Method for grouping the consecutive numbers
    '''                                                      
    iters = tee(iterable, n)                                                     
    for i, it in enumerate(iters):                                               
        next(islice(it, i, i), None)                                               
    return zip(*iters)

def count_consecutive_summers(num):
    rng = range(1, num+1)
    #print(list(rng))
    counter = 0
    
    for i in range(num + 1):
        list_of_groups = list(grouping(rng, i))
        for item in list_of_groups:
            if sum(item) == num:
                #print(item)
                counter += 1
    
    print(num, counter)
    return counter


# Mathematical Solution:
# https://py.checkio.org/mission/count-consecutive-summers/publications/Phil15/python-3/v3-count-odd-divisors/?ordering=most_voted&filtering=all

# Well, I saw that what we want is equal to the number of odd divisors of n so...
#count_consecutive_summers = lambda n: sum(not n%k for k in range(1, n+1, 2))

def count_consecutive_summers_(num):
    result = sum(not num%k for k in range(1, num+1, 2))
    print(num, result)
    return sum(not num%k for k in range(1, num+1, 2))
    


# Another Best Solution:
# https://py.checkio.org/mission/count-consecutive-summers/publications/arggg55/python-3/first/share/e638f0afdde094eed27fda63c65589c3/

def count_consecutive_summers_(num):
    # your code here
    count = 0
    for i in range(1, num+1):
        add = i
        sum = 0
        while sum <= num :
            sum += add
            add += 1
            if sum == num:
                count += 1
    return count



if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    assert count_consecutive_summers(15) == 4
    assert count_consecutive_summers(4096) == 1
    assert count_consecutive_summers(1575) == 18
    assert count_consecutive_summers(2835) == 20
    print("Coding complete? Click 'Check' to earn cool rewards!")