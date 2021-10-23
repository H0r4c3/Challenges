'https://www.hackerrank.com/challenges/minimum-distances/problem?h_r=internal-search'

my_list = [0, 1, 2, 3, 4, 2, 5, 6, 7, 3, 8]

duplicates_dict = dict()
distances = list()
min_dist = 0

def minimum_distance(my_list):
    i = 0
    n = len(my_list)
    # The distance between two array values is the number of indices between them.
    for x in range(i, n):
        for y in range(i+1, n):
            if (my_list[x] == my_list[y] and x<y):
                distances.append(abs(x-y))
                res = min(distances)
    if distances == []:
        res = -1
                
    return res

min_dist = minimum_distance(my_list)
print(min_dist)