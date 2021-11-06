'https://py.checkio.org/en/mission/correct-sentence/'

'''
For the input of your function, you will be given one sentence. You have to return a corrected version, 
that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary. 
If a sentence already ends with a period (dot), then adding another one will be a mistake.
'''

def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    result = text[0].upper() + text[1:]
    if text[-1] != '.':
        result = result + '.'
    
    return result


if __name__ == '__main__':

    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."