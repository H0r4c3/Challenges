'https://py.checkio.org/en/mission/useless-flights/'

'''
Here you have a flight schedule by which you need to find out whether all flights are really necessary.
'''

from typing import List

def all_nodes(schedule):
    nodes = set()
    for item in schedule:
        nodes.add(item[0])
        nodes.add(item[1])
    
    nodes = sorted(list(nodes))
    return nodes

def useless_flight(schedule: List) -> List:
    print(schedule)
    
    nodes = all_nodes(schedule)
    print(nodes)
    
    # make a dictionary with every node as key, and a list of connections for every node, as value
    schedule_dict = dict()

    for sublist in schedule:
        if sublist[0] not in schedule_dict.keys():
            schedule_dict[sublist[0]]=[sublist]
        else:
            schedule_dict[sublist[0]].append(sublist)
    
    schedule_dict = dict(sorted(schedule_dict.items()))     
    print(schedule_dict)
    
    # make a dictionary with the number of connections for every node
    nodes_connections_dict = {node:len(schedule_dict[node]) for node in nodes[:-1]}
    print(nodes_connections_dict)
    
    #route = list()
    # for node in nodes[:-1]:
    #     # list of connections from the first node
    #     a = schedule_dict.get(node)
    #     print(a)
    #     for connection in a:
    #         route.append(connection)
    route = list()
    for i in range(2):
        route[i].extend(schedule_dict[nodes[0]][i])
    
    print(route)
    
    
    
    
    return None


# ChatGPT Solution: NOK!!!
# https://chat.openai.com/chat

def useless_flight_(connections):
    n = len(connections)
    unnecessary_flights = []
    for i in range(n):
        for j in range(i+1, n):
            if connections[i][0] == connections[j][0] and connections[i][1] == connections[j][1]:
                if connections[i][2] <= connections[j][2]:
                    unnecessary_flights.append(j)
                else:
                    unnecessary_flights.append(i)
    print(unnecessary_flights)
    return unnecessary_flights




# Best Solution: 
# https://py.checkio.org/mission/useless-flights/publications/Freez/python-3/recursive/?ordering=most_voted&filtering=all

from typing import List


def find_cheaper_route(max_price: int, current_point, destination_point, schedule):
    schedule = [flight for flight in schedule if flight[2] < max_price]
    if not schedule:
        return False
    for flight in schedule:
        if flight[1] == destination_point and flight[0] == current_point:
            return True

    for flight in schedule:
        if current_point == flight[0] and find_cheaper_route(max_price - flight[2], flight[1], destination_point,
                                                             schedule):
            return True
    return False


def useless_flight_(schedule: List) -> List:
    for i in range(len(schedule)):
        schedule.append([schedule[i][1], schedule[i][0], schedule[i][2]])
    return [i for i, flight in enumerate(schedule) if
            i < len(schedule) // 2 and find_cheaper_route(flight[2], flight[0], flight[1], schedule)]




if __name__ == '__main__':
    print("Example:")
    #print(useless_flight([['A', 'B', 50], ['B', 'C', 40], ['A', 'C', 100]]))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert useless_flight([['A', 'B', 50],['B', 'C', 40],['A', 'C', 100]]) == [2]
    #assert useless_flight([['A', 'B', 50],['B', 'C', 40],['A', 'C', 90]]) == []
    #assert useless_flight([['A', 'B', 50],['B', 'C', 40], ['A', 'C', 40]]) == []
    assert useless_flight([['A', 'C', 10],
                           ['C', 'B', 10],
                           ['C', 'E', 10],
                           ['C', 'D', 10],
                           ['B', 'E', 25],
                           ['A', 'D', 20],
                           ['D', 'F', 50],
                           ['E', 'F', 90]]) == [4, 7]
    
    print("Coding complete? Click 'Check' to earn cool rewards!")