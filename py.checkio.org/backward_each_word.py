'https://py.checkio.org/en/mission/backward-each-word/'

'''
In a given string, you should reverse every word, but the words should stay in their places.
'''

def backward_string_by_word(text: str) -> str:
    text_list1 = list()
    text_list = text.split(' ')
    for item in text_list:
        item1 = item[::-1]
        text_list1.append(item1)
    
    result = ' '.join(text_list1) 
    
    return result


if __name__ == '__main__':
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'