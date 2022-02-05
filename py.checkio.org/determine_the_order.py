'https://py.checkio.org/en/mission/determine-the-order/'

'''
You have a set of "words", all in lower case, and each word contains symbols in "alphabetical order". (it's not your typical alphabetical order, 
but a new and different order.) We need to determine the order of the symbols from each "word" and create a single "word" with all of these symbols, 
placing them in the new alphabetical order. In some cases, if we cannot determine the order for several symbols, 
you should use the traditional latin alphabetical order . 
For example: Given words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a" and "d" after "b". So the result is "zwacbd".
'''
from collections import OrderedDict
from typing import List

def checkio(data=List[str]):
    data = [''.join(OrderedDict.fromkeys(d)) for d in data]
    print(f'data = {data}')
    
    data_unique = sorted(set(''.join(data)))
    print(f'data_unique = {data_unique}')
    
    result = ""
    while data_unique:
        for c in data_unique:
            if not any(c in d[1:] for d in data):
                result += c
                break
        
        data = [d.replace(c, "") for d in data]
        data_unique.remove(c)
        
    print(f'result = {result}')
    return result


# Best Solution: https://py.checkio.org/mission/determine-the-order/publications/Sim0000/python-3/simple/?ordering=most_voted&filtering=all
def checkio(data):
    alphabet = sorted(set(''.join(data))) # unique alphabet
    result = ''
    for n in range(len(alphabet)):
        # find minimum
        for c in alphabet:
            if c in result: continue # already used
            if all(c not in word or c == word[0] for word in data): break # found
        result += c
        # remove c from data
        for i in range(len(data)): data[i] = data[i].replace(c, '')
    return result




#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", "Concatenate and paste in"