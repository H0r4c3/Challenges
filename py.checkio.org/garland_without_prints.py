'https://py.checkio.org/en/mission/garland/share/ee8c1f57f95077bf136d79a490095173/'

'''
Your task is to turn on as few individual lights as possible so that every position of the entire row is illuminated by at least one light.
'''

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
        illuminated_all = illuminated_all.union(illuminated)
        
        # eliminate the negative numbers and the numbers > len(lights)
        illuminated_all = set([item for item in illuminated_all if (item >= 0 and item < len(lights))])
        
    return illuminated_all
        
    
def illuminate_all(lights: list[int]) -> int:
    all_comb_indexes = all_combinations(lights)
    
    for list_of_indexes in all_comb_indexes:
        illuminated_all = turn_on_lights(lights, list_of_indexes)
        if len(lights) == len(illuminated_all):
            return len(list_of_indexes)


print("Example:")
#print(illuminate_all([0, 0]))

# These "asserts" are used for self-checking
assert illuminate_all([1, 2, 3, 4]) == 1
assert illuminate_all([0, 0]) == 2
assert illuminate_all([2, 3, 3, 2]) == 1
assert illuminate_all([1, 0, 1, 0]) == 2
assert illuminate_all([0, 0, 2, 3, 4, 1, 0, 1, 2, 2, 5, 2, 3, 0, 1, 0, 0]) == 3
assert illuminate_all([0, 2, 2, 2, 2, 0, 1, 2, 0, 0, 1, 1, 1, 0, 1, 0, 0, 2, 1, 1, 0, 1, 1, 2, 0, 0, 1]) == 8

print("The mission is done! Click 'Check Solution' to earn rewards!")