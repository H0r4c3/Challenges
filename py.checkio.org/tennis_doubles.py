'https://py.checkio.org/en/mission/tennis-doubles/'

'''
Four friends have agreed to play doubles tennis. 
Each of the friends has a level of play, which is represented by a positive integer: the higher the number, the better the player's level.
'''

def level_dif(levels: list[int]) -> int:
    dif = abs((sorted(levels)[-1] + sorted(levels)[0]) - (sorted(levels)[-2] + sorted(levels)[1]))
    print(dif)
    return dif


print("Example:")
print(level_dif([1, 2, 3, 4]))

# These "asserts" are used for self-checking
assert level_dif([1, 2, 3, 4]) == 0
assert level_dif([5, 5, 5, 5]) == 0
assert level_dif([1, 9, 3, 2]) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")