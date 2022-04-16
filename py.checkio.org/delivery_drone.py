'https://py.checkio.org/en/mission/delivery-drone/'

'''
The input value is a list of integers. One or more numbers of this list represent the existence of the package(s) to be transported and its destination. 
You have to return the shortest moving distance for the drone to complete all transportation as an integer.

Note:
The drone is initially at position 0 (far-left position).
The drone can carry only one package at a time.
You can drop the package only at the destination point.
You aren't forced to pick up the package at the destination point.
The drone returns to position 0.
'''

from typing import List


def delivery_drone(orders: List[int]) -> int:

    return 0



# Best Solution: 
# https://py.checkio.org/mission/delivery-drone/publications/Tinus_Trotyl/python-3/first/share/3871c8446133abcaf395c3a1274add4c/

from typing import List
from itertools import permutations

def delivery_drone(orders: List[int]) -> int:
    distance = 0
    for workflow in permutations(package for package in orders if package):
        moves, position = 0, 0
        for package in workflow:
            pickup = orders.index(package)
            moves += abs(pickup - position) + abs(package - pickup)
            position = package
        moves += position
        distance = min(distance, moves) if distance else moves   
    return distance



if __name__ == '__main__':
    assert delivery_drone([0, 2, 0]) == 4
    assert delivery_drone([0, 0, 1, 2]) == 6
    assert delivery_drone([0, 2, 4, 0, 1, 0, 5]) == 12
    print('The local tests are done. Click on "Check" for more real tests.')