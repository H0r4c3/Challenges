'https://py.checkio.org/en/mission/secret-message/'

'''
You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.

For example: text = " H ow are you? E h, ok. L ow or L ower? O hhh.", if we collect all of the capital letters, we get the message "HELLO".

Input: A text as a string (unicode).

Output: The secret message as a string or an empty string.
'''

import re
def find_message_(message: str) -> str:
    regex = re.compile('[A-Z]+')
    result = regex.findall(message)
    print(result)
    
    return ''.join(result)


# Shorter version
def find_message(message: str) -> str:
    return ''.join(re.findall('[A-Z]+', message))



# https://py.checkio.org/mission/secret-message/publications/gyahun_dash/python-3/first/?ordering=most_voted&filtering=all

def find_message_(message):
    return ''.join(c for c in message if c.isupper())



if __name__ == '__main__':
    print("Example:")
    #print(find_message(('How are you? Eh, ok. Low or Lower? '+ 'Ohhh.')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_message(('How are you? Eh, ok. Low or Lower? '+ 'Ohhh.')) == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("Coding complete? Click 'Check' to earn cool rewards!")