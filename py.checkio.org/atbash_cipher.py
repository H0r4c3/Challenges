'https://py.checkio.org/en/mission/atbash-cipher/'

'''
Atbash is one of the oldest known ciphers, created in Middle East around 600 B.C.;
The substitution table (for Latin alphabet) looks like this:

    Plaintext alphabet:  abcdefghijklmnopqrstuvwxyz
    Ciphertext alphabet: zyxwvutsrqponmlkjihgfedcba
    
To decrypt a message, the same algorithm is applied to the ciphertext.

Input: plaintext: str

Output: ciphertext: str
'''

def atbash(plaintext: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cypher = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
    new_text = ''
    
    for item in plaintext:
        if item not in alphabet:
            new_text = new_text + item
        else:
            index = alphabet.find(item)
            new_text = new_text + cypher[index]
    
    return new_text

    
    


if __name__ == "__main__":
    print("Example:\nplaintext: testing")
    print(atbash("testing"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert atbash("testing") == "gvhgrmt"
    assert atbash("attack at dawn") == "zggzxp zg wzdm"
    assert atbash("Hello, world!") == "Svool, dliow!"
