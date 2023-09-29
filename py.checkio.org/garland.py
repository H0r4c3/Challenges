'https://py.checkio.org/en/mission/garland/share/ee8c1f57f95077bf136d79a490095173/'

'''
Your task is to turn on as few individual lights as possible so that every position of the entire row is illuminated by at least one light.
'''

# My Solution (Error = Time) - must be optimized!!!!!!!!!

import timeit
from itertools import combinations

def all_combinations(lights):
    '''
    create a list of all combinations of indexes of lights in list of lights
    '''
    indexes = list(range(0, len(lights)))
    all_comb_indexes = [list(item) for i in range(1, len(lights)+1) for item in combinations(indexes, i)]
    return all_comb_indexes


def indexes_illuminated(lights, idx):
    '''
    create a list with all indexes that are illuminated by the light at index idx
    '''
    power = lights[idx]
    illuminated = set(range(idx-power, idx+power+1))
    
    return illuminated 
    

def turn_on_lights(lights, list_of_indexes):
    '''
    turn on the lights having indexes in the list_of_indexes and check if every position is illuminated
    '''
    illuminated_all = set()
    for idx in list_of_indexes:
        illuminated = indexes_illuminated(lights, idx)
        print(f'illuminated = {illuminated}')
        illuminated_all = illuminated_all.union(illuminated)
        
        # eliminate the negative numbers and the numbers > len(lights)
        illuminated_all = set([item for item in illuminated_all if (item >= 0 and item < len(lights))])
        
    return illuminated_all
        
    
def illuminate_all(lights: list[int]) -> int:
    starttime = timeit.default_timer()
    
    print('-------------------')
    print(f'lights = {lights}')
    print('-------------------')
    all_comb_indexes = all_combinations(lights)
    print(f'all_comb_indexes = {all_comb_indexes}')
    duration1_seconds = timeit.default_timer() - starttime
    
    for list_of_indexes in all_comb_indexes:
        print(f'*** New list_of_indexes = {list_of_indexes} for the list {lights}')
        illuminated_all = turn_on_lights(lights, list_of_indexes)
        print(f'illuminated_all = {illuminated_all}')
        if len(lights) == len(illuminated_all):
            duration_seconds = timeit.default_timer() - starttime
            duration_minutes = duration_seconds / 60
            print(f'duration1_seconds for all_combinations = {duration1_seconds}')
            print(f'duration_seconds = {duration_seconds}')
            return len(list_of_indexes)
        else:
            print(f'Only {len(illuminated_all)} lights are illuminated, instead of all lights = {len(lights)}')


# BEST Solution: https://py.checkio.org/mission/garland/publications/kdim/python-3/combinations/?ordering=most_voted&filtering=all

from itertools import combinations

def illuminate_all(lights: list[int]) -> int:
    l = len(lights)
    for i in range(1, l + 1):
        for j in combinations(range(l), i):
            illuminate = {m + n for m in j for n in range(-lights[m], lights[m] + 1) if l > m + n >= 0}
            if len(illuminate) == l:
                return i


  

print("Example:")
#print(illuminate_all([0, 0]))

# These "asserts" are used for self-checking
assert illuminate_all([1, 2, 3, 4]) == 1
assert illuminate_all([0, 0]) == 2
assert illuminate_all([2, 3, 3, 2]) == 1
assert illuminate_all([1, 0, 1, 0]) == 2
assert illuminate_all([0, 0, 2, 3, 4, 1, 0, 1, 2, 2, 5, 2, 3, 0, 1, 0, 0]) == 3
#[4, 10, 16]
#assert illuminate_all([0, 2, 2, 2, 2, 0, 1, 2, 0, 0, 1, 1, 1, 0, 1, 0, 0, 2, 1, 1, 0, 1, 1, 2, 0, 0, 1]) == 8
# [2, 7, 11, 14, 17, 19, 23, 26]

print("The mission is done! Click 'Check Solution' to earn rewards!")