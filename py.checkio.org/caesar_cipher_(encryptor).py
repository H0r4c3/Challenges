'https://py.checkio.org/en/mission/caesar-cipher-encryptor/'

'''
Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher 
where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"
'''

def to_encrypt(text, delta):
    result = ''
    for item in text:
        if item == ' ':
            result += item
        else:
            new_ord = 97 + ((ord(item) - 97 + delta) % 26)
            result += chr(new_ord)
        
    return result


# the best solution:
def to_encrypt(text, delta):
    from string import ascii_lowercase as alphabet
    shifted = alphabet[delta:] + alphabet[:delta]
    return text.translate(str.maketrans(alphabet, shifted))


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"