'https://py.checkio.org/en/mission/friends/'

'''
For the mission "How to find friends" , it’s nice to have access to a specially made data structure. In this mission we will realize a data structure which we will use to store and work with a friend network.

The class "Friends" should contains names and the connections between them. Names are represented as strings and are case sensitive. 
Connections are undirected, so if "sophia" is connected with "nikola", then it's also correct in reverse.
'''

class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)
            return True
        else:
            return False

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        return {i for item in self.connections for i in item}

    def connected(self, name):
        #conn = set()
        # for item in self.connections:
        #         if name in item:
        #             item.remove(name)
        #             conn.add(list(item)[0])
        # return conn
    
        return {conn for conn in self.names() if {conn, name} in self.connections}


friend1 = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
print(friend1.connections)
friend1.add({"c", "d"})
print(friend1.connections)   
friend1.remove({"c", "d"})
print(friend1.connections)
print(friend1.names())
    


# Best Solution:
# https://github.com/denisbalyko/checkio-solution/blob/master/friends.py

class Friends_:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        return set().union(*self.connections)

    def connected(self, name):
        return {n for n in self.names() if {n, name} in self.connections}
    
    
    
# Another Best Solution: 
# https://py.checkio.org/mission/friends/publications/gyahun_dash/python-3/set/?ordering=most_voted&filtering=all

class Friends_(set):
    def __init__(self, pairs=set()):
        super().__init__(map(frozenset, pairs))

    def add(self, pair):
        if pair in self: return False
        super().add(frozenset(pair))
        return True

    def remove(self, pair):
        if pair not in self: return False
        super().remove(pair)
        return True

    def names(self):
        return set().union(*self)

    def connected(self, name):
        return Friends(filter({name}.issubset, self)).names() - {name}



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    print('Done!!!')