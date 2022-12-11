'https://py.checkio.org/en/mission/power-supply/'

'''
Input: Two arguments. The first one is the network, represented as a list of connections. 
Each connection is a list of two nodes that are connected. A city or power plant can be a node. 
Each city or power plant is a unique string. The second argument is a dict where keys are power plants and values are the power plant's range.

Output: A set of strings. Each string is the name of a blacked out city.
'''

def power_supply_(network, power_plants):
    return set([])



# Best Solution:
# https://py.checkio.org/mission/power-supply/publications/kdim/python-3/8-lines/?ordering=most_voted&filtering=all


def power_supply(network, power_plants):
    nodes, connected = set(sum(network, [])), set()
    for plant, power in power_plants.items():
        connect = set([plant])
        for _ in range(power):
            connect |= set(i[n == i[0]] for i in network for n in connect if n in i)
        connected |= connect
    return nodes - connected




if __name__ == "__main__":
    assert power_supply([["p1", "c1"], ["c1", "c2"]], {"p1": 1}) == set(["c2"]), "one blackout"
    assert power_supply([["c0", "c1"], ["c1", "p1"], ["c1", "c3"], ["p1", "c4"]], {"p1": 1}) == set(["c0", "c3"]), "two blackout"
    assert power_supply([["p1", "c1"], ["c1", "c2"], ["c2", "c3"]], {"p1": 3}) == set([]), "no blackout"
    assert power_supply([["c0", "p1"], ["p1", "c2"]], {"p1": 0}) == set(["c0", "c2"]), "weak power-plant"
    assert power_supply([["p0", "c1"], ["p0", "c2"], ["c2", "c3"], ["c3", "p4"], ["p4", "c5"]],{"p0": 1, "p4": 1},) == set([]), "cooperation"
    assert power_supply(
        [
            ["c0", "p1"],
            ["p1", "c2"],
            ["c2", "c3"],
            ["c2", "c4"],
            ["c4", "c5"],
            ["c5", "c6"],
            ["c5", "p7"],
        ],
        {"p1": 1, "p7": 1},
    ) == set(["c3", "c4", "c6"]), "complex cities 1"
    assert power_supply(
        [
            ["p0", "c1"],
            ["p0", "c2"],
            ["p0", "c3"],
            ["p0", "c4"],
            ["c4", "c9"],
            ["c4", "c10"],
            ["c10", "c11"],
            ["c11", "p12"],
            ["c2", "c5"],
            ["c2", "c6"],
            ["c5", "c7"],
            ["c5", "p8"],
        ],
        {"p0": 1, "p12": 4, "p8": 1},
    ) == set(["c6", "c7"]), "complex cities 2"
    assert power_supply([["c1", "c2"], ["c2", "c3"]], {}) == set(
        ["c1", "c2", "c3"]
    ), "no power plants"
    assert power_supply(
        [["p1", "c2"], ["p1", "c4"], ["c4", "c3"], ["c2", "c3"]], {"p1": 1}
    ) == set(["c3"]), "circle"
    assert power_supply([["p1", "c2"], ["p1", "c4"], ["c2", "c3"]], {"p1": 4}) == set(
        []
    ), "more than enough"
    print("Looks like you know everything. It is time for 'Check'!")