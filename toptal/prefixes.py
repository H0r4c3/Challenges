'''
Given a list of names, determine the number of names in that list for which a given query string is a prefix. 
The prefix must be at least 1 character less that the entire name string
Example
names = ['jackson', 'jacques', 'jack']
query = ['jack']
The complete query string 'jack' is a prefix of jackson but not of jacques of jack. The prefix cannot contain the entire name string, so 'jack' does not qualify.
'''

def prefix(names=list[str], query=list[str]) -> int:
    counter = 0
    q = query[0]
    for item in names:
        if item.startswith(q) and len(item) > len(q):
            counter += 1
    
    print(counter)
    return counter


if __name__ == '__main__':
    assert prefix(['jackson', 'jacques', 'jack'], ['jack']) == 1

