'https://py.checkio.org/en/mission/network-loops/'

'''
A routing loop is a common problem with computer networks. Loops are virtually the same as cycles in graphs. 
For this mission, we’ll learn how to find these cycles in a network.

A cycle consists of a sequence of nodes starting and ending on the same node without repetition and 
with each consecutive node in the sequence connecting to each other in the network. The cycle length is the quantity of nodes within the cycle. 
The length of cycle will always be greater than 2. 
You should find the largest cycle in a given network, determine if we have multiple equal sized loops, then choose any one of them.
'''

def find_cycle(connections):
    return []



# Best Solution:
# https://py.checkio.org/mission/network-loops/publications/Sim0000/python-3/first/share/0b59f7c54b2e0e340375b48eab64d40c/

from collections import deque

def find_cycle(network):
    all_node = set(sum(network, ()))
    max_path = ()
    network = [set(relation) for relation in network]
    for goal in all_node:
        # BFS
        q = deque([(goal,)])
        while q:
            path = q.popleft()
            if len(path) > 1 and path[-1] == goal: # found cycle
                if len(path) <= 3: continue # bad cycle, for example a-b-a
                if len(path) > len(max_path): max_path = path # new record
                continue
            for next in all_node: # register next path
                if (next not in path or next == goal) and {path[-1], next} in network:
                    q.append(path + (next,))
    return max_path


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(function, connections, best_size):
        user_result = function(connections)
        if not isinstance(user_result, (tuple, list)) or not all(isinstance(n, int) for n in user_result):
            print("You should return a list/tuple of integers.")
            return False
        if not best_size and user_result:
            print("Where did you find a cycle here?")
            return False
        if not best_size and not user_result:
            return True
        if len(user_result) < best_size + 1:
            print("You can find a better loop.")
            return False
        if user_result[0] != user_result[-1]:
            print("A cycle starts and ends in the same node.")
            return False
        if len(set(user_result)) != len(user_result) - 1:
            print("Repeat! Yellow card!")
            return False
        for n1, n2 in zip(user_result[:-1], user_result[1:]):
            if (n1, n2) not in connections and (n2, n1) not in connections:
                print("{}-{} is not exist".format(n1, n2))
                return False
        return True, "Ok"
    
    assert checker(find_cycle, 
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6),
                    (8, 5), (8, 4), (1, 5), (2, 4), (1, 8)), 6), "Example"
    assert checker(find_cycle, 
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6), (8, 4), (1, 5), (2, 4)), 5), "Second"
    print('Done!!!')