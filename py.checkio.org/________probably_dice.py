'https://py.checkio.org/en/mission/probably-dice/'

'''
Tips: Be careful if you want to use a brute-force solution -- you could have a very, very long wait for edge cases.

Input: Three arguments. The number of dice, the number of sides per die and the target number as integers.

Output: The probability of getting exactly target number on a single roll of the given dice as a float.
'''

def probability(dice_number, sides, target):
    
    return 0



# Best Solution: 
# https://py.checkio.org/mission/probably-dice/publications/przemyslaw.daniel/python-3/8-liner-cleanest-recursive/?ordering=most_voted&filtering=all

from functools import lru_cache

@lru_cache(maxsize=None)
def probability(dice_number, sides, target):
    if dice_number == 1:
        return (1 <= target <= sides**dice_number)/sides
    return sum([probability(dice_number-1, sides, target-x)
                for x in range(1, sides+1)])/sides



if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
