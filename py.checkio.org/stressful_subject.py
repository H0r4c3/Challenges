'https://py.checkio.org/en/mission/stressful-subject/'

'''
The function should recognize if a subject line is stressful. 
A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains 
at least one of the following “red” words: "help", "asap", "urgent". Any of those "red" words can be spelled in 
different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP," they just can't have 
any other letters interspersed between them.

Input: Subject line as a string.

Output: Boolean.
'''
import re
def is_stressful(subj=str):
    """
        recognize stressful subject
    """
    if subj.isupper():
        return True
    pattern = re.compile('!!!$|help|asap|urgent|h+[^\w]*e+[^\w]*l+[^\w]*p+|a+[^\w]*s+[^\w]*a+[^\w]*p+|u+[^\w]*r+[^\w]*g+[^\w]*e+[^\w]*n+[^\w]*t+', re.I)
    result = pattern.search(subj)
    print(result)
    
    return True if result else False


# One-liner solution: https://py.checkio.org/mission/stressful-subject/publications/martin_b/python-3/find-a-bug-/?ordering=most_voted&filtering=all
def is_stressful_(s):
    return s.isupper() or s.endswith('!!!') or any(re.search("+\W*".join(w), s, re.I) for w in ("help", "asap", "urgent"))


if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("I neeed H!E!L!P!") == True
    assert is_stressful("I neeed HHHEEEEEEEEELLP") == True
    assert is_stressful("I neeed HxExLxP") == False
    assert is_stressful("where are you?!!!!") == True
    assert is_stressful("Heeeeeey!!! I’m having so much fun!”") == False
    assert is_stressful("HI HOW ARE YOU?") == True
    print('Done! Go Check it!')