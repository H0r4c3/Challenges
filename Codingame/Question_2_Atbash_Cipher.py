

def atbash(word: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cypher = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
    new_text = ''
    
    for item in word:
        if item not in alphabet:
            new_text = new_text + item
        else:
            index = alphabet.find(item)
            new_text = new_text + cypher[index]
    
    return new_text

word = 'zyxabc'

print(atbash(word))