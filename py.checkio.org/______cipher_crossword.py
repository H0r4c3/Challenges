'https://py.checkio.org/en/mission/cipher-crossword/'

'''
Input: The Cipher Crossword as a list of lists with integers. Words as a list of strings.

Output: The solution to the Crossword as a list of lists with letters.
'''


def checkio(crossword, words):
    pass




# Best Solution:
# https://py.checkio.org/mission/cipher-crossword/publications/gyahun_dash/python-3/userdict/share/2a2e4e3027b42d9cffa127741f5e98f2/

from collections import UserDict
from itertools import chain, permutations

class ConsistentDict(UserDict):
    def __setitem__(self, key, item):
        if not key in self.keys(): self.data[key] = item
        elif self[key] != item: raise ValueError #prohibit updates

def enumerate_numbers_on(grid): #line: rows[0, 2, 4], columns[0, 2, 4]
    for line in chain(grid[::2], list(zip(*grid))[::2]): yield from line

#arrange numbers in a line, and find consistent mapping(brute force)
def checkio(crossword, words):
    line = list(enumerate_numbers_on(crossword))
    for candidate_words in permutations(words):
        try: cdict = ConsistentDict(zip(line, ''.join(candidate_words)))
        except ValueError: continue
        else: return [[cdict.get(n, ' ') for n in row] for row in crossword]


if __name__ == "__main__":
    assert checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6],
        ],
        ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
    ) == [
        ["h", "e", "l", "l", "o"],
        ["a", " ", "e", " ", "z"],
        ["b", "i", "m", "b", "o"],
        ["i", " ", "m", " ", "n"],
        ["t", "r", "a", "c", "e"],
    ]