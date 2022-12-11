'https://py.checkio.org/en/mission/most-wanted-letter-2/'

'''
If you have two or more letters occurring the same number of times , then return all of them as a list. 
For example -- "Hello, Evan" should return ['e', 'l'].

Input: A text for analysis as a string.

Output: The list of the most frequent letters in lowercase.
'''

def most_wanted(text: str) -> str:
    text = text.lower()
    text_dict = {letter : text.count(letter) for letter in text if letter.isalpha()}
    print(text_dict)
    text_max = [key for key, value in text_dict.items() if value == max(text_dict.values())]
    
    print(text_max)
    return text_max

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sorted(most_wanted("Hello World!")) == ["l"], "Hello test"
    assert sorted(most_wanted("How do you do?")) == ["o"], "O is most wanted"
    assert sorted(most_wanted("One")) == ["e", "n", "o"], "All letter only once."
    assert sorted(most_wanted("Oops!")) == ["o"], "Don't forget about lower case."
    assert sorted(most_wanted("AAaooo!!!!")) == ["a", "o"], "Only letters."
    assert sorted(most_wanted("abe")) == ["a", "b", "e"], "The First."
    print("Start the long test")
    assert sorted(most_wanted("a" * 9000 + "b" * 1000)) == ["a"], "Long."
    print("The local tests are done.")