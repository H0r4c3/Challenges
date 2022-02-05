'https://py.checkio.org/en/mission/the-longest-palindromic/'

'''
Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!

If you find more than one substring, you should return the one that’s closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.
'''

from itertools import combinations
def longest_palindromic(a):
    
    all_substrings = sorted([a[i:j] for i, j in combinations(range(len(a) + 1), r=2)], key=len, reverse=True)
    #all_substrings.sort(key=len, reverse=True)
    #print(all_substrings)
    
    for item in all_substrings:
        if item == item[::-1]:
            print(item)
            return item


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")