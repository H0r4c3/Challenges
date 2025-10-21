'https://py.checkio.org/en/mission/string-2-matrix/'

'''
You are given an unsorted string of unique (ignoring case) lower- and/or uppercase letters. 
Represent it as a correct mask for the square-arranged letters of the alphabet from "a" to "y" (row-major order). 
The mask must be a 5x5 matrix of integers as tuple of tuples with the following rule.

character is not present in the string - use 0 in mask;
character is lowercase - use 1;
character is uppercase - use 2.
'''

Row = tuple[int, int, int, int, int]
Grid = tuple[Row, Row, Row, Row, Row]

ALPHABET = (('a', 'b', 'c', 'd', 'e'),
            ('f', 'g', 'h', 'i', 'j'),
            ('k', 'l', 'm', 'n', 'o'),
            ('p', 'q', 'r', 's', 't'),
            ('u', 'v', 'w', 'x', 'y'))

def find_position(letter):
    for i in range(5):
        for j in range(5):
            if ALPHABET[i][j] == letter.lower():
                return(i, j)

def converter(text: str) -> Grid:
    START = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]
    
    print(f'-----START: text = {text}')
    for letter in text:
        pos = find_position(letter)
        print(f'letter = {letter}')
        print(f'position = {pos}')
        START[pos[0]][pos[1]] = 1 if letter.islower() else 2
        
    result = tuple([tuple(row) for row in START])
    print(result)
    print()
    
    return result


print("Example:")
#print(converter("sMcigkqow"))

# These "asserts" are used for self-checking
assert converter("sMcigkqow") == (
    (0, 0, 1, 0, 0),
    (0, 1, 0, 1, 0),
    (1, 0, 2, 0, 1),
    (0, 1, 0, 1, 0),
    (0, 0, 1, 0, 0),
)
assert converter("acSyIwoQkumGe") == (
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1),
)

assert converter('cdeyfkmphrtAjovuw') == (
    (2, 0, 1, 1, 1), 
    (1, 0, 1, 0, 1), 
    (1, 0, 1, 0, 1), 
    (1, 0, 1, 0, 1), 
    (1, 1, 1, 0, 1))

print("The mission is done! Click 'Check Solution' to earn rewards!")