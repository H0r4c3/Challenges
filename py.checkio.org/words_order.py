'https://py.checkio.org/en/mission/words-order/'

'''
You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.

Cases you should expect while solving this challenge:

a word from the list is not in the text - your function should return False;
any word can appear more than once in a text - use only the first one;
two words in the given list are the same - your function should return False;
the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
the text includes only English letters and spaces.
Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool.
'''

def words_order(text: str, words: list) -> bool:
    indexes = list()
    text_list = text.split()
    for item in words:
        if item in text_list:
            index = text_list.index(item)
            indexes.append(index)
        else:
            return False
    
    
    if len(words) != len(set(words)):
        return False
    
    if indexes == sorted(indexes):
        return True
    else:
        return False
    
    
    
    


if __name__ == '__main__':
    
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here', ['world', 'here', 'hi']) == False
    assert words_order('hi world im here', ['world', 'im', 'here']) == True
    assert words_order('hi world im here', ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here', ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False