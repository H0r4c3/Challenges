'https://www.hackerrank.com/challenges/sparse-arrays/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign'

'''
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
'''

def matchingStrings(strings, queries):
    counter = []
    for item in queries:
        #print(strings.count(item))
        counter.append(strings.count(item))
        
    return counter

strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']

result = matchingStrings(strings, queries)
for item in result:
    print(item)