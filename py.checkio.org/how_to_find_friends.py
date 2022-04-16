'https://py.checkio.org/en/mission/find-friends/'

'''
Your should write a function that allow determine more complex connection between drones. 
You are given two names also. Try to determine if they are related through common bonds by any depth.
'''

def links(network, name):
    ''' find the connections for each drone'''
    links_list = list()
    for item in network:
        if name in item:
            links_list.append(item.split('-'))
            
    links_list = [item for it in links_list for item in it] # flatten the list of lists
    links_set = set(links_list) # transform the list in a set
    print(f'links_set_{name} = {links_set}')
    return links_set

def all_links(network, name):
    ''' find the connections for all connections for name'''
    links_set_total = set()
    links_set = links(network, name)
    
    for name in links_set:
        print(name)
        links_set = links(network, name)
        links_set_total = links_set_total.union(links_set)
    
    for _ in range(len(links_set)):    
        for name in links_set_total:
            links_set = links(network, name)
            links_set_total = links_set_total.union(links_set)
        
    return links_set_total



def check_connection(network, first, second):
    print(network)
    
    links_set_total_1 = all_links(network, first)
    print(f'links_set_total_1 = {links_set_total_1}')
    links_set_total_2 = all_links(network, second)
    print(f'links_set_total_2 = {links_set_total_2}')
    result = links_set_total_1.intersection(links_set_total_2)  
    
    print(f'result = {result}')
    return True if result else False




# Best Solution
# https://py.checkio.org/mission/find-friends/publications/StefanPochmann/python-3/bellman-ford-ish-short/?ordering=most_voted&filtering=all

def check_connection_(network, first, second):
    team = {first}
    for _ in network:
        for edge in network:
            pair = set(edge.split('-'))
            if pair & team:
                team |= pair
    return second in team


# Best Solution
# https://py.checkio.org/mission/find-friends/publications/Sim0000/python-3/first/share/1f08cfe46d817f5d5ce79a68fabae8d6/

def check_connection_(network, first, second):
    setlist = []
    for connection in network:
        s = ab = set(connection.split('-'))
        # unify all set related to a, b
        for t in setlist[:]: # we need to use copy
            if t & ab:       # check t include a, b
                s |= t
                setlist.remove(t)
        setlist.append(s)    # only s include a, b
    return any(set([first, second]) <= s for s in setlist)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(("scout2-scout5", "scout1-scout3", "scout3-scout4", "scout4-scout5"), "scout1", "scout2") == True
    
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
    assert check_connection(("scout2-plane1","plane1-stevan","stevan-night","night-mega",
                      "mega-sscout","sscout-super","super-scout3","scout3-doc","doc-batman",),"scout2","batman")
    
    print('Done!!!')