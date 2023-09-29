'https://py.checkio.org/en/mission/nonogram-encode/share/589d8dd0030475ae20329329c8324a80/'

'''
Your goal is to create a nonogram from the image: write a number clue for solving this image like it was hidden. 
Your function should return a list of two lists. 
The first one consists of lists with numbers for columns clue, the second one - the same for rows clue. 
All lists in columns clue, as well as in rows, should be of same 'depth' (complemented with 0).
'''

def nonogram_encode(data: list[str]) -> list[list[list[int]]]:
    # your code here
    return []


print("Example:")
print(nonogram_encode([" X X ", "X X X", " X X "]))

# These "asserts" are used for self-checking
assert nonogram_encode([" X X ", "X X X", " X X "]) == [
    [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
    [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
]
assert nonogram_encode(["X"]) == [[[1]], [[1]]]

print("The mission is done! Click 'Check Solution' to earn rewards!")