'https://py.checkio.org/en/mission/middle-characters/'

'''
You are given some string where you need to find its middle characters. The string may contain one word, a few symbols or a whole sentence. 
If the length of the string is even, then you should return two middle characters, but if the length is odd, return just one.
'''

def middle(text:str):
    le = len(text)
    result = text[(le - 1) // 2 : (le + 2) // 2]
    print(result)
    
    #return text[(len(text) - 1) // 2 : (len(text) + 2) // 2]
    return result

if __name__ == '__main__':
    print("Example:")
    #print(middle('example'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'    
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")