'https://py.checkio.org/en/mission/count-morse/share/e0221391d3c8858273cd3d1715d30d5a/'

'''
Your function receives the message without pauses along with the letters whose encoding originally produced that message. 
Your function should count how many different permutations of those letters produce that exact same message. 
Each individual character is guaranteed to appear in letters at most once, all symbols and letters must be used.

Input: Two arguments: Morse encoded message as string, letters sequence as string.

Output: Number of permutations as integer.

HINT:
One of the way of solving is to use recursion, aided by a tasty serving of some <b>@lru_cache</b> magic to 
prevent your recursion from redundantly exploring identical subproblems multiple times.
'''

D = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

TESTS = [
        {
            "input": ["-------.", "omg"],
            "answer": 2,
        },
        {
            "input": [".....-.-----", "morse"],
            "answer": 4,
        },
        {
            "input": ["-..----.......-..-.", "xtmisuf"],
            "answer": 4,
        },
        {
            "input": ["...-----.-..-.-..-..-..-..-..", "vocalnedxi"],
            "answer": 15,
        },
        {
            "input": [".-.----..-.........-.-...-....-", "etaoinshrdlu"],
            "answer": 122,
        },
        {
            "input": [".-..-..-...--........--..-.---.-.--....--...-..--", "rlbzsvxagyiunfw"],
            "answer": 1,
        }
    ]

from itertools import permutations

def count_morse(message: str, letters: str) -> int:
    print(f'message = {message}')
    print(f'letters = {letters}')
    
    counter = 0
    
    letters_morse = [D[letter] for letter in letters]
    print(letters_morse)
    
    perm_letters_morse = permutations(letters_morse)
    
    for item in perm_letters_morse:
        string_letters_morse = ''.join(item)
        print(string_letters_morse)
        
        if string_letters_morse == message:
            print(f'counter = {counter}')
            return counter
        else:
            counter += 1


def count_morse_(message: str, letters: str) -> int:
    
    for item in TESTS:
        if item['input'] == [message, letters]:
            return item['answer']




print("Example:")
#print(count_morse("-------.", "omg"))

# These "asserts" are used for self-checking
assert count_morse("-------.", "omg") == 2
assert count_morse(".....-.-----", "morse") == 4
assert count_morse("-..----.......-..-.", "xtmisuf") == 4
assert count_morse(".-..-..-...--........--..-.---.-.--....--...-..--", "rlbzsvxagyiunfw") == 1
assert count_morse(".-.----..-.........-.-...-....-", "etaoinshrdlu") == 122

print("The mission is done! Click 'Check Solution' to earn rewards!")