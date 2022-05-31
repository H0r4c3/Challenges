'https://py.checkio.org/en/mission/the-stones/'

'''
You most likely know the game where two players are in turn taking from a pile from 1 to 3 stones, and loses the one who took the last stone. We'll slightly generalize this task. Let's assume that both players can take not 1, 2, 3 stones, but k1, k2, …, km of stones. Here we are interested which player wins under the right circumstances (the game played properly and both players use the best strategy).
As the input you will get the number of stones in the pile at the beginning of the game and an amounts of stones you can take from pile at each move. For example - (10, [1, 2, 3]).
If the current amount of the stones in the pile is lower than lowest number in the "moves" list or equal to it - current player takes them all and lose.
'''

def stones(pile, moves):
    #replace this for solution
    return 0


# Best Solution:
# https://py.checkio.org/mission/the-stones/publications/Merzix/python-3/4-liner/share/35aa737e04c8b59c28b87ee79482847f/
    
def stones(pile, moves):
    game = {x: False for x in range(1, moves[0] + 1)}  # True if 1st player wins if x rocks in pile
    
    for stone in range(moves[0] + 1, pile + 1):
        game[stone] = any(not game[stone - m] for m in moves if stone > m)
        
    return (2,1)[game[pile]]


if __name__ == '__main__':
    print("Example:")
    print(stones(17, [1, 3, 4]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stones(17, [1, 3, 4]) == 2
    assert stones(17, [1, 3, 4, 6, 9]) == 1
    assert stones(99, [1]) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
