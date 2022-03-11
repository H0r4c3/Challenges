'https://py.checkio.org/en/mission/four-to-the-floor/'

'''
Given a room's size and a list of PIR sensors mounted on the room's ceiling and looking down on the floor, 
your task is to determine whether the floor area is completely into the sensors coverage area (return True) or not (return False). 
The bottom left corner of the rectangle matches the origin point O , the top right corner is defined by W and H . 
Each sensor is defined by its mounting point (coordinates x i and y i ) and its range ( R i ).

Input: Two arguments:

the first is a list containing a room's top right corner coordinates,all are integers [W, H]
the second is a list containing sensors info, all are integers [[x i , y i , R i ], [x i+1 , y i+1 , R i+1 ], ....., [x n , y n , R n ]]
Output: True or False.
'''

# Best Solution:
# https://py.checkio.org/mission/four-to-the-floor/publications/Oleg_Domokeev/python-3/first/share/f69aaaae18cc93159441d55e47b16343/

def is_covered(room, sensors):
    
    def in_circles(i, j):
        for x0, y0, R in sensors:
            if (i - x0) ** 2 + (j - y0) ** 2 <= R ** 2:
                return True
        return False
    
    for x in range(room[0] + 1):
        for y in range(room[1] + 1):
            if not in_circles(x, y):
                return False
    return True


if __name__ == "__main__":
    print("Example:")
    print(is_covered([200, 150], [[100, 75, 130]]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_covered([200, 150], [[100, 75, 130]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True
    assert (
        is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False
    )
    assert (
        is_covered(
            [200, 150],
            [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]],
        )
        == True
    )
    assert (
        is_covered(
            [200, 150],
            [[100, 75, 100], [0, 40, 50], [0, 110, 50], [200, 40, 50], [200, 110, 50]],
        )
        == False
    )
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 110]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 20]]) == False
    assert is_covered([3, 1], [[1, 0, 2], [2, 1, 2]]) == True
    assert (
        is_covered([30, 10], [[0, 10, 10], [10, 0, 10], [20, 10, 10], [30, 0, 10]])
        == True
    )
    assert (
        is_covered([30, 10], [[0, 10, 8], [10, 0, 7], [20, 10, 9], [30, 0, 10]]) == False)
        
    assert (is_covered([300,150],[[40,60,240],[240,140,100],[295,10,50]]) == False)
    
    print("Coding complete? Click 'Check' to earn cool rewards!")

