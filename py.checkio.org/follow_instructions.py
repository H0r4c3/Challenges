'https://py.checkio.org/en/mission/follow-instructions/'

'''
In this mission you should follow a given list of instructions which will get you to a certain point on the map. 
A list of instructions is a string, each letter of this string points you in the direction of your next step.

The letter "f" - tells you to move forward, "b" - backward, "l" - left, and "r" - right.

It means that if the list of your instructions is "fflff" then you should move forward two times, make one step to the left and then again move two times forward.

Now, let's imagine that you are in the position (0,0). If you move forward your position will change to (0, 1). 
If you move again it will be (0, 2). If your next step is to the left then your position will become (-1, 2). 
After the next two steps forward your coordinates will be (-1, 4)

Your goal is to find your final coordinates. Like in our case they are (-1, 4)

Input: A string.

Output: A tuple (or list) of two ints
'''

from typing import Tuple

def follow_H(instructions: str) -> Tuple[int, int]:
    coordinates = [0, 0]

    for item in instructions:
        if item == 'f':
            coordinates[1] += 1
            continue
        if item == 'b':
            coordinates[1] -= 1
            continue
        if item == 'r':
            coordinates[0] += 1
            continue
        if item == 'l':
            coordinates[0] -= 1
         
    return tuple(coordinates)
        


# The best solution:
# https://py.checkio.org/mission/follow-instructions/publications/Sim0000/python-3/count/?ordering=most_voted&filtering=all
            
def follow(instructions):
    c = instructions.count
    return c('r') - c('l'), c('f') - c('b')



if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")