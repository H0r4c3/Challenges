'https://py.checkio.org/en/mission/caesar-cipher-decryptor/'

'''
Your mission is to decrypt a secret message (which consists of text, the whitespace characters and special chars like "!", "&", "?" etc.) 
using Caesar cipher where each letter is replaced by another that stands at a fixed distance. 
For example ("a b c", 3) == "d e f". Also you should ignore/delete all special characters. 
So the message like this ("!d! [e] &f*", -3) will be decrypted just as "a b c" and nothing more.
'''

import re

def to_decrypt(cryptotext, delta):
    result = list()
    regex = re.compile('[\s?\w+\s?]')
    cryptotext_ok = regex.findall(cryptotext)
    for item in cryptotext_ok:
        if item == ' ':
            result.append(item)
        elif item == '_':
            pass
        else:
            new_ord = 97 + ((ord(item) - 97 + delta) % 26)
            result.append(chr(new_ord))
            
    print(cryptotext_ok)
    print(result)
    
    return ''.join(result)


# Another solution:
# https://py.checkio.org/mission/caesar-cipher-decryptor/publications/veky/python-3/punctuation-as-junk/?ordering=most_voted&filtering=all#comment-109909
def to_decrypt_(text, delta):
    from string import ascii_lowercase as alphabet, punctuation as junk
    shifted = alphabet[delta:] + alphabet[:delta]
    return text.translate(str.maketrans(alphabet, shifted, junk))
            
        
    
    

if __name__ == '__main__':
    print("Example:")
    print(to_decrypt('abc', 10))
    print(to_decrypt('!d! [e] &f*', -3))
    print(to_decrypt('x^$# y&*( (z):-)', 3))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print('Done!')