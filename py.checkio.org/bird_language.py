'https://py.checkio.org/en/mission/bird-language/'

'''
The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.

Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
A phrase always has the translation.
'''

import re

def translate(text: str) -> str:
    result = ''
    
    vowels = 'aeiouy'
    consonants = 'bcdfghjklmnpqrstvwxz'
    
    # text = re.sub('[a]{3}', 'a', text)
    # text = re.sub('[e]{3}', 'e', text)
    # text = re.sub('[i]{3}', 'i', text)
    # text = re.sub('[o]{3}', 'o', text)
    # text = re.sub('[u]{3}', 'u', text)
    # text = re.sub('[y]{3}', 'y', text)
    
    for vowel in vowels:
        text = re.sub(vowel + '{3}', vowel, text)
        
    for cons in consonants:
        text = re.sub(cons + '[aeiouy]', cons, text)
    
    print(text)
    
    return text


# A new method: https://py.checkio.org/mission/bird-language/publications/veky/python-3/partial/#comments
def translate_short(text: str) -> str:
    import re, functools
    
    translate = functools.partial(re.sub, r"(\w)(\1\1|.)", r"\1")
    
    return translate


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))
    print(translate("hoooowe yyyooouuu duoooiiine"))

    #These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"