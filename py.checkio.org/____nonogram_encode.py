'https://py.checkio.org/en/mission/nonogram-encode/share/589d8dd0030475ae20329329c8324a80/'

'''
Your goal is to create a nonogram from the image: write a number clue for solving this image like it was hidden. 
Your function should return a list of two lists. The first one consists of lists with numbers for columns clue, 
the second one - the same for rows clue. All lists in columns clue, as well as in rows, should be of same 'depth' (complemented with 0).
'''

def line_encode(my_data):
    line_enc = [len(item) for item in ''.join(my_data).split(' ') if len(item)]
    return line_enc


def complement_lists(my_data):
    '''
    All lists in columns clue, as well as in rows, should be of same 'depth' (complemented with 0).
    '''
    complement = [[0] * (max([len(item) for item in my_data]) - len(item)) + item for item in my_data]
    return complement


def nonogram_encode(data: list[str]) -> list[list[list[int]]]:
    print(f'START data = {data}')
    
    rows, columns = len(data), len(data[0])
    
    col1 = [[data[r][c] for c in range(columns)] for r in range(rows)]
    print(f'col1 = {col1}')
    
    row1 = [[data[r][c] for r in range(rows)] for c in range(columns)]
    print(f'row1 = {row1}')
    
    line_enc_col = [line_encode([data[r][c] for c in range(columns)]) for r in range(rows)]
    print
    line_enc_row = [line_encode([data[r][c] for r in range(rows)]) for c in range(columns)]
    
    
    col = complement_lists([line_encode([data[r][c] for c in range(columns)]) for r in range(rows)])
    row = complement_lists([line_encode([data[r][c] for r in range(rows)]) for c in range(columns)])
    print(f'col = {col}')
    print(f'row = {row}')
    
    nonogram = [[list(item) for item in zip(*row)], col]
    print(f'nonogram = {nonogram}')
    
    return nonogram



# Best Solution:
# https://py.checkio.org/mission/nonogram-encode/publications/tokiojapan55/python-3/first/?ordering=most_voted&filtering=all

def nonogram_encode_(data: list[str]) -> list:
    line_encode = lambda d: [len(s) for s in "".join(d).split(" ") if len(s)]
    adjust = lambda d: [[0] * (max([len(v) for v in d]) - len(v)) + v for v in d]

    if data:
        ROWS, COLS = len(data), len(data[0])
        col = adjust([line_encode([data[r][c] for c in range(COLS)]) for r in range(ROWS)])
        row = adjust([line_encode([data[r][c] for r in range(ROWS)]) for c in range(COLS)])
        return [[list(v) for v in zip(*row)], col]
    return []


print("Example:")
#print(nonogram_encode([" X X ", "X X X", " X X "]))

# These "asserts" are used for self-checking
assert nonogram_encode([" X X ", "X X X", " X X "]) == [
    [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
    [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
]
assert nonogram_encode(["X"]) == [[[1]], [[1]]]

assert nonogram_encode([' X X ', 'X X X', ' X X ']) == [[[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]], [[0, 1, 1], [1, 1, 1], [0, 1, 1]]]

print("The mission is done! Click 'Check Solution' to earn rewards!")