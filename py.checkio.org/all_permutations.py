'https://py.checkio.org/en/mission/all-permutations/'

'''
Given a string, return all possible permutations of its characters, sorted alphabetically.
'''

from collections.abc import Iterable
from itertools import permutations


def string_permutations(s: str) -> Iterable[str]:
    perm = [''.join(item) for item in permutations(s)]
    perm_ordered = sorted(perm)
    print(perm_ordered)
    return perm_ordered


print("Example:")
#print(list(string_permutations("ab")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")