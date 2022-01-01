'https://py.checkio.org/en/mission/the-cheapest-flight/'

'''
As the input you get the flight schedule as an array, each element of which is the price of a direct 
flight between 2 cities (an array of 3 elements - 2 city names as a string, and a flight price).

Planes fly in both directions and the price in both directions is the same. There is a possibility that there are no direct flights between cities.

Find the price of the cheapest flight between cities that are given as the 2nd and 3rd arguments.

Input: 3 arguments: the flight schedule as an array of arrays, city of departure and destination city.

Output: Int. The best price.
'''

from typing import List


def cheapest_flight(costs: List, a: str, b: str) -> int:
    route = [([i], a) for i in costs if a in i]
    price = 999
    while route:
        flight, lastPosition = route.pop(0)
        st, ed, pr = flight[-1]
        currentPosition = ed if st == lastPosition else st
        if b in (st, ed):
            price = min(price, sum([pr for _, _, pr in flight]))
        else:
            for nextStep in [i for i in costs if currentPosition in i and i not in flight]:
                route.append((flight + [nextStep], currentPosition))
    return price if price != 999 else 0


# def cheapest_flight(costs: List, a: str, b: str) -> int:
#     costs = sorted(costs)
#     costs_dict = {item[0] + item[1] : item[2] for item in costs}
#     dest = sorted(a + b)
#     dest = dest[0] + dest[1]
    
#     print(costs_dict)
#     print(dest)
    
    
    #return costs[2]


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100], ['A', 'B', 20], ['B', 'C', 50]],'A','C'))
    print(cheapest_flight([['A', 'C', 40], ['A', 'B', 20], ['A', 'D', 20], ['B', 'C', 50], ['D', 'C', 70]],'D','C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100], ['A', 'B', 20], ['B', 'C', 50]], 'A','C') == 70
    assert cheapest_flight([['A', 'C', 100], ['A', 'B', 20], ['B', 'C', 50]], 'C','A') == 70
    assert cheapest_flight([['A', 'C', 40], ['A', 'B', 20], ['A', 'D', 20], ['B', 'C', 50], ['D', 'C', 70]],'D','C') == 60
    assert cheapest_flight([['A', 'C', 100], ['A', 'B', 20], ['D', 'F', 900]], 'A', 'F') == 0
    assert cheapest_flight([['A', 'B', 10], ['A', 'C', 15], ['B', 'D', 15], ['C', 'D', 10]], 'A', 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")