'https://py.checkio.org/en/mission/matrix-2-string/'

'''
You are given a 5x5 matrix of integers as tuple of tuples. 
Use it as a mask for the square-arranged letters of the alphabet from "a" to "y" (row-major order). 
Return a string of characters (sorted, ignore case), picked from the square of letters according to the mask with the following rule:

0 in mask - do not take the respective character;
1 - take in lowercase;
2 - take in uppercase.
'''

Row = tuple[int, int, int, int, int]
Grid = tuple[Row, Row, Row, Row, Row]

ALPHABET = (('a', 'b', 'c', 'd', 'e'),
            ('f', 'g', 'h', 'i', 'j'),
            ('k', 'l', 'm', 'n', 'o'),
            ('p', 'q', 'r', 's', 't'),
            ('u', 'v', 'w', 'x', 'y'))


def converter(matrix: Grid) -> str:
    result = ''
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                result += ALPHABET[i][j]
            elif matrix[i][j] == 2:
                result += ALPHABET[i][j].upper()
    print(result)
    return result


print("Example:")
print(
    converter(
        (
            (0, 0, 1, 0, 0),
            (0, 1, 0, 1, 0),
            (1, 0, 2, 0, 1),
            (0, 1, 0, 1, 0),
            (0, 0, 1, 0, 0),
        )
    )
)

# These "asserts" are used for self-checking
assert (
    converter(
        (
            (0, 0, 1, 0, 0),
            (0, 1, 0, 1, 0),
            (1, 0, 2, 0, 1),
            (0, 1, 0, 1, 0),
            (0, 0, 1, 0, 0),
        )
    )
    == "cgikMoqsw"
)
assert (
    converter(
        (
            (1, 0, 1, 0, 1),
            (0, 2, 0, 2, 0),
            (1, 0, 1, 0, 1),
            (0, 2, 0, 2, 0),
            (1, 0, 1, 0, 1),
        )
    )
    == "aceGIkmoQSuwy"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")