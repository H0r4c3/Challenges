'https://py.checkio.org/en/mission/revorse-the-vewels/'

'''
Given a text string, create and return a new string constructed by finding all its vowels and reversing their order, 
while keeping all other characters exactly as they were in their original positions. 
'''

def reverse_vowels(text: str) -> str:
    # print(f'----text = {text}')
    # text_enum = list(enumerate(text))
    # print(text_enum)
    
    text_vocals = [v.lower() for v in text if v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
    print(f'text_vocals = {text_vocals}')
    
    vocals_replace = text_vocals[::-1]
    print(f'vocals_replace = {vocals_replace}')
    
    #text_enum_vocals = [e for e in text_enum if e[1] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
    #print(f'text_enum_vocals = {text_enum_vocals}')
    
    text_new = list()
    for i in range(len(text)):
        if text[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            if text[i].islower():
                text_new += vocals_replace[0]
                vocals_replace.pop(0)
            else:
                text_new += vocals_replace[0].upper()
                vocals_replace.pop(0)  
        else:
            text_new += text[i]
            
    result = ''.join(text_new)        
    print(f'result = {result}')
    
    return result

# Best Solution: 
# https://py.checkio.org/mission/revorse-the-vewels/publications/tokiojapan55/python-3/first/?ordering=most_voted&filtering=all

def reverse_vowels_(text: str) -> str:
    isvowel = lambda c: c.lower() in "aeiou"
    setcase = lambda v, c: v.upper() if c.isupper() else v.lower()
    vowels = [c for c in list(text) if isvowel(c)]
    return ''.join(c if not isvowel(c) else setcase(vowels.pop(), c) for c in list(text))


print("Example:")
print(reverse_vowels("Hello, World"))

# These "asserts" are used for self-checking
assert reverse_vowels("Bengt Hilgursson") == "Bongt Hulgirssen"
assert (
    reverse_vowels("Why do you laugh? I chose death.")
    == "Why da yee loigh? U chasu dooth."
)
assert (
    reverse_vowels("These are the people you protect with your pain!")
    == "Thisa uro thi peoplu yoe protect weth year peen!"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")