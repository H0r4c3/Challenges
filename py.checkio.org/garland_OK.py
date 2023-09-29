'https://py.checkio.org/en/mission/garland/share/ee8c1f57f95077bf136d79a490095173/'

'''
Your task is to turn on as few individual lights as possible so that every position of the entire row is illuminated by at least one light.
'''

# My Solution

from itertools import combinations            

def illuminate_all(lights: list[int]) -> int:
    print(f'*****lights = {lights}')
    nr_lights = len(lights)

    for group in range(1, nr_lights + 1):
        print(f'group = {group}')
        combs = combinations(range(nr_lights), group)
        for co in combs:
            illuminate = {c + x for c in co for x in range(-lights[c], lights[c] + 1) if nr_lights > c + x >= 0}
            if len(illuminate) == nr_lights:
                return group

    

print("Example:")
#print(illuminate_all([0, 0]))

# These "asserts" are used for self-checking
assert illuminate_all([1, 2, 3, 4]) == 1
#assert illuminate_all([0, 0]) == 2
assert illuminate_all([2, 3, 3, 2]) == 1
assert illuminate_all([1, 0, 1, 0]) == 2
assert illuminate_all([0, 0, 2, 3, 4, 1, 0, 1, 2, 2, 5, 2, 3, 0, 1, 0, 0]) == 3
#[4, 10, 16]
assert illuminate_all([0, 2, 2, 2, 2, 0, 1, 2, 0, 0, 1, 1, 1, 0, 1, 0, 0, 2, 1, 1, 0, 1, 1, 2, 0, 0, 1]) == 8
# [2, 7, 11, 14, 17, 19, 23, 26]

print("The mission is done! Click 'Check Solution' to earn rewards!")