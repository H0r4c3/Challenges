'https://py.checkio.org/en/mission/the-highest-building/'

'''
Input: Heights of the buildings as a 2D-array.

Output: The number of the highest building and height of it as a list of integers 

(Important: in this task the building numbers starts from "1", not from "0")
'''
import numpy as np
def highest_building(buildings):
    result = list()
    sum_arr = np.sum(buildings, axis=0)
    print(sum_arr)
    max_height = max(sum_arr)
    position = np.argmax(sum_arr) + 1
    result.append(position)
    result.append(max_height)
    
    return result

# A shorter version
def highest_building_(buildings):
    sum_arr = np.sum(buildings, axis=0)
    
    return [np.argmax(sum_arr) + 1, max(sum_arr)]


# Another solution: https://py.checkio.org/mission/the-highest-building/publications/przemyslaw.daniel/python-3/3-liner-yawning/?ordering=most_voted&filtering=all
def highest_building_(data):
    data = list(map(sum, zip(*data)))
    return [data.index(max(data))+1, sum(max(data))]



if __name__ == '__main__':
    print("Example:")
    print(highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == [3, 4], "Common"
    assert highest_building([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]) == [4, 1], "Cabin in the wood"
    assert highest_building([
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]
    ]) == [1, 5], "Triangle"
    assert highest_building([
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]) == [4, 6], "Pyramid"
    print("Coding complete? Click 'Check' to earn cool rewards!")