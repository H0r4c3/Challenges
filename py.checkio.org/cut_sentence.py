'https://py.checkio.org/en/mission/cut-sentence/'

'''
Your task in this mission is to truncate a sentence to a length that does not exceed a given number of characters.

If the given sentence already is short enough, you don't have to do anything to it. But if it needs to be truncated, 
the omission must be indicated by concatenating an ellipsis ("...") to the end of the shortened sentence.

The shortened sentence can contain complete words and spaces.
It must neither contain truncated words nor trailing spaces.
The ellipsis has been taken into account for the allowed number of characters, so it does not count against the given length.
'''

def cut_sentence(line: str, length: int) -> str:
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    if length >= len(line):
        return line
    
    for i in range (length, 0, -1):
        if line[i] == ' ':
            return line[:i] + '...'
        
    return '...'



# Best Solution:
# https://py.checkio.org/mission/cut-sentence/publications/andreyihnatchenko/python-3/first/share/dceca765a48d0395ec46646ec6d3861a/

def cut_sentence_(line, length):
    if length >= len(line):
        return line
    for i in range (length, 0, -1):
        if line[i] == ' ':
            return line[:i] + '...'
    return '...'



# Another BEST Solution:
# https://py.checkio.org/mission/cut-sentence/publications/kurosawa4434/python-3/resubver2/?ordering=most_voted&filtering=all

from re import sub

def cut_sentence(line, length):
    if len(line) > length:
        return sub(' *[^ ]*$', '...', line[:length+1])
    else:
        return line



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')