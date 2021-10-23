'Test Topal - www.hackerrank.com'

'''
Given a list of names, determine the number of names in that list for which a given query string is a prefix. 
The prefix must be at least 1 character less than the entire name string

Example:
names = ['jackson', 'jacques', 'jack', 'john', 'johnson', 'jill']
query = ['jack', 'jo']

The function must return an array of integers that each denotes the number of names strings for which a query string is a prefix
'''

from typing import Counter


def findCompletePrefixes(names, query):
    counter = []
    for q in query:
        c = 0
        for item in names:
            if q in item:
                if len(q) != len(item):
                    c += 1
                    print(item)
        counter.append(c)
        
                    
    return counter

names = ['jackson', 'jacques', 'jack', 'john', 'johnson', 'jill']
query = ['jack', 'jo', 'po', 'j']

counter = findCompletePrefixes(names, query)
print(counter)