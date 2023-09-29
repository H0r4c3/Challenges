'https://py.checkio.org/en/mission/rolling/share/e7e48ad23b19f556d8e35fe5e5585f85/'

'''
There is a standard 6-sided 🎲, which looks and placed as shown below. It may be rolled in four cardinal directions: North, South, West, East.
For the mission you are given a string moves with directions. You need to find out, what side of 🎲 is on top after rolling.

Input: String with directions of rolling.

Output: Number of side, which is on top.
'''
def rotation_left(my_list):
    # W or S
    # using slicing to left rotate by 1
    new_list = my_list[1:] + my_list[:1]
    return new_list

def rotation_right(my_list):
    # E or N
    # using slicing to right rotate by 1
    new_list = my_list[-1:] + my_list[:-1]
    return new_list

def one_roll(x, y, move):
    if move == 'E':
        x = rotation_right(x)     # [1, 3, 6, 4] -> [4, 1, 3, 6]
        y[0], y[1], y[2], y[3] = x[0], y[1], x[2], y[3] # [1, 5, 6, 2] -> [4, 5, 3, 2]
    elif move == 'W':
        x = rotation_left(x)      # [1, 3, 6, 4] -> [3, 6, 4, 1]
        y[0], y[1], y[2], y[3] = x[0], y[1], x[2], y[3] # [1, 5, 6, 2] ->  [3, 5, 4, 2]
    elif move == 'N':
        y = rotation_right(y)     # [1, 5, 6, 2] -> [2, 1, 5, 6]  
        x[0], x[1], x[2], x[3] = y[0], x[1], y[2], x[3] # [1, 3, 6, 4] -> [2, 3, 5, 4] # positions 1 and 3 stay unchanged, positions 0 and 2 are same with rotation_right(y)
    elif move == 'S':
        y = rotation_left(y)      # [1, 5, 6, 2] -> [5, 6, 2, 1]
        x[0], x[1], x[2], x[3] = y[0], x[1], y[2], x[3] # [1, 3, 6, 4] -> [5, 3, 2, 4] # positions 1 and 3 stay unchanged, positions 0 and 2 are same with rotation_left(y)
    return x, y
        
def rolling_dice(moves: str) -> int:
    x = [1, 3, 6, 4] # WE axis
    y = [1, 5, 6, 2] # SN axis
    
    for move in moves:
        x, y = one_roll(x, y, move)
    
    print(x, y)
    print(x[0])
    
    return x[0]
        

# Best Solutions:
 
# https://py.checkio.org/mission/rolling/publications/przemyslaw.daniel/python-3/11-liner-unrolling/?ordering=most_voted&filtering=all

def rolling_dice(moves: str) -> int:
    top, front, right = 1, 2, 3
    for move in moves:
        top, front, right = {
            "N": (front, -top, right),
            "S": (-front, top, right),
            "W": (right, front, -top),
            "E": (-right, front, top),
        }[move]

    return top % 7


# https://py.checkio.org/mission/rolling/publications/amandel/python-3/straightforward-fsm/?ordering=most_voted&filtering=all

def rolling_dice(moves: str) -> int:
    t,f,r = 1,2,3  # top, front, right, kept mod 7
    for x in moves:
        t,f,r = {'N':(f,-t,r), 'S':(-f,t,r), 'E':(-r,f,t), 'W':(r,f,-t)}[x]
    return t if t > 0 else 7+t



print("Example:")
#print(rolling_dice("SE"))

# These "asserts" are used for self-checking
assert rolling_dice("SN") == 1
assert rolling_dice("") == 1
assert rolling_dice("EESWN") == 6
assert rolling_dice("NWSNWEESNW") == 3
assert rolling_dice("NNNSESNESWNENSWNNWSWNSSNWWSWNW") == 5
assert rolling_dice('SSSS') == 1
assert rolling_dice('SSS') == 2
assert rolling_dice('WENWNNSSSE') == 2
assert rolling_dice('SSENNWWEES') == 5
assert rolling_dice('NNNSESNESWNENSWNNWSWNSSNWWSWNW') == 5
assert rolling_dice('WSWNENSNSEWESEESNWEW') == 2
assert rolling_dice('ESWWNNNNSEENWSENNWNW') == 2
assert rolling_dice('SENWNSENSESSSEWNENWSNSENWNNWNNNWWESESESNWE') == 2
assert rolling_dice('SNNNWSSSESWNWSWSENNWNNSNWNENWEWSESNENWNNW') == 6
assert rolling_dice('ESWNNNWWSNSNNESWSWEWENNNSESENNWNENWSWNSENNWSW') == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")