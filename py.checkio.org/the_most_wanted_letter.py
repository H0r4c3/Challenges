'https://py.checkio.org/en/mission/most-wanted-letter/'

'''
You are given a text, which contains different English letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency , then return the letter which comes first in the Latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.
'''

import re
import string
from collections import Counter


def checkio(text: str) -> str:
    text_low = ''.join(sorted(text.lower()))
    
    regex = re.compile('[a-z]+')
    text_low_letters = re.findall(regex, text_low)
    
    char_counts = Counter(text_low_letters[0])
    dict_ord = dict(char_counts.most_common())
    
    return list(dict_ord.keys())[0]


# https://py.checkio.org/mission/most-wanted-letter/publications/bryukh/python-3/max-count/?ordering=most_voted&filtering=choice
def checkio_BEST(text):
    """
    We iterate through latin alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter, 'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)



if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")