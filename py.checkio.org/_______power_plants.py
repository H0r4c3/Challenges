'https://py.checkio.org/en/mission/power-plants/'

'''
You have to properly place the given power plants and supply power to all the cities.
'''

from typing import Set, Tuple, List, Dict

def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    network_list = [(item) for item in network]
    print(network_list)
    
    all_cities = {item for tup in network for item in tup}
    all_cities_list = sorted(list(all_cities))
    print(all_cities_list)
    
    # dictionary with all the cities as keys having as values all the tuples with neighbors
    network_dict1 = {key:{item for item in network_list if key in item} for key in all_cities_list}
    print(network_dict1)
    
    # flatten the tuples in values set
    network_dict2 = {key:{item for subitem in value for item in subitem} for key, value in network_dict1.items()}
    print(network_dict2)
    
    # transform the values in a list having only the neighbors of the keys (cities)
    #network_dict3 = {key:sorted(list(value)) for key, value in network_dict2.items()}
    network_dict3 = {key:[val for val in value if val != key] for key, value in network_dict2.items()}
    print(network_dict3)
    
    # sort the dict after the length of the values
    sorted_value_key_pairs = sorted(network_dict3.items(), key=lambda x: len(x[1]), reverse=True)
    print(sorted_value_key_pairs)
    
    # recreate the dictionary, now, sorted
    network_dict_sorted = {value:key for value, key in sorted_value_key_pairs}
    print(network_dict_sorted)
    
    print(list(network_dict_sorted.keys())[0])
    
    result = dict()
    for i in ranges:
        result[list(network_dict_sorted.keys())[0]] = i
        
    print(result)
    
    return result


# Best Solution:
# https://py.checkio.org/mission/power-plants/publications/Ylliw/python-3/first-fully-documented-great-mission/?ordering=most_voted&filtering=all

from typing import Set, Tuple, List, Dict
from itertools import chain,combinations
from collections import namedtuple

def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    # Let's rework the ranges in a dict containing each power and it's number of occurences
    # Order this dict with greater power first
    powers={power:ranges.count(power) for power in sorted(set(ranges),reverse=True)}
    # Let's define a list of cities
    cities=set(chain(*network))
    
    def network_map(max_power: int) -> Dict[str, Dict[int, List[str]]]:
        '''
        A network map, giving for each city a dict of cities within range of x
        {City_A:{0:[City_A],1:[some_cities],2:[some_more_cities]},City_B:...}

        Will stop the map for a max of 'max_power' moves as we can used any further info
        '''
        # First build a dict of cities reachable in 1 move from each city
        reachable_in_one={city:set() for city in cities}
        for city_a,city_b in network:
            reachable_in_one[city_a]|={city_b}
            reachable_in_one[city_b]|={city_a}
        # Let's construct our very first cities_map, each city can reach only itself in 0 move
        cities_map={city:{0:set(city)} for city in cities}

        # We have to loop 'max_power' time to ensure we have build the full map
        for distance in range(0,max_power):
            for city in cities:
                # All Cities reachable from city in exactly 'distance' moves
                reachable={city_b for city_a in cities_map[city][distance] for city_b in reachable_in_one[city_a]}
                # We have to add the cities reachable in les than 'distance' moves, but we already computed that
                cities_map[city][distance+1]=reachable|cities_map[city][distance]
        return cities_map

    # So build our nice cities map
    cities_map=network_map(max(powers))
    # Each step consits in unpowered cities, powered cities, already placed plants, remaining power plant to set
    # namedtuple allows a convenient used of those informations
    Step=namedtuple('Step',['unpowered','powered','plants','powers'])
    # First step is no city powered, no plants and the full powers list
    steps=[Step(unpowered=set(cities),powered=set(),plants=dict(),powers=powers)]
    # Run until we haven't found the answer or there is no more steps to test
    # Steps are ordered with most interesting (so far) ones at the end
    while steps:
        step=steps.pop()
        # We are looking to assign the power 'power' a certain number of time
        power=max(step.powers)
        nb_occurences=step.powers[power]

        if len(step.unpowered)<=nb_occurences:
            # No need to continue any longer, we just have to power the unpowered cities:
            return {**step.plants,**{city:power for city in step.unpowered}}
        # Let's pick all combinations of nb_occurences in the unpowered cities
        for combination in combinations(step.unpowered,nb_occurences):
            powered=set()
            plants=dict(step.plants)
            for city in combination:
                powered|=cities_map[city][power]
                plants[city]=power
            unpowered=step.unpowered-powered
            if unpowered:
                # Still some city unpowered, let's see what power remains
                powers=dict(step.powers)
                del powers[power]
                if powers:
                    # Still some power plants to assign, so let's add this possibility
                    powered|=step.powered
                    steps.append(Step(unpowered=unpowered,powered=powered,plants=plants,powers=powers))
            else:
                # Bingo all cities are powered
                return plants
            
        # We have check all combinations, none being finished
        # let's order possible next steps:
        # The less powered situation at start, so that best powered are at end (picked first)
        # If equal, the one with less remaining plants (powers) at start so that most options are picked first
        steps.sort(key=lambda step:(len(step.powered),len(powers)))

    # If we reach this points, there was no proper answer, so let's say we found nothing
    return dict()




if __name__ == '__main__':
    assert power_plants({('A', 'B'), ('B', 'C')}, [1]) == {'B': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

    print('The local tests are done. Click on "Check" for more real tests.')