'https://py.checkio.org/mission/the-most-frequent/publications/add/'

'''
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.

Input: a list of strings.

Output: a string.
'''

from collections import Counter

def most_frequent_(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    string_counts = Counter(data)
    frequency = string_counts.most_common()
    
    return frequency[0][0]



# Best Solution: https://py.checkio.org/mission/the-most-frequent/publications/veky/python-3/my-favorite-way-of-solving-oduvans-missions-p/?utm_source=digest&utm_medium=email&utm_campaign=digest
from statistics import mode
def most_frequent(data: list) -> str:
    return mode(data)


# Another Best Solution: https://py.checkio.org/mission/the-most-frequent/publications/kdim/python-3/max-set/#comment-116079
def most_frequent(data: list) -> str:
    return max(set(data), key=data.count)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
    
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')