'https://py.checkio.org/en/mission/count-inversions/'

'''
You are given a sequence of unique numbers and you should count the number of inversions in this sequence.
'''

# My first Solution
from itertools import combinations
def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    comb = list(combinations(sequence, 2))
    inv = [item for item in comb if item[1] < item[0]]
    
    print(len(inv))
    return len(inv)


# My second Solution
def count_inversion_(sequence):
    """
        Count inversions in a sequence of numbers
    """
    counter = 0
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if sequence[j] < sequence[i]:
                counter += 1
    
    return counter




if __name__ == '__main__':
    print("Example:")
    #print(count_inversion([1, 2, 5, 3, 4, 7, 6]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")