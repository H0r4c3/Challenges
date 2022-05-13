'https://py.checkio.org/en/mission/wild-dogs/'

'''
As input you’ll be given the coordinates of the dogs. 
Your task is to find the distance to the nearest point from which you can kill the maximum 
number of animals with one shot (any number of dogs on the same line can be killed with one shot). 
Your starting position is the point (0, 0).
'''

def wild_dogs(coords):
    #replace this for solution
    return 0



# Best Solution: 
# https://py.checkio.org/mission/wild-dogs/publications/Moff/python-3/first/share/326a46c7ae0a7e8a731f9c35fbbbe96b/

def wild_dogs_(dogs):
    dist = mx = 0
    for p1 in dogs:
        for p2 in dogs:
            if p1 != p2:
                a, b, c = p1[1] - p2[1], p2[0] - p1[0], p1[0] * p2[1] - p2[0] * p1[1]
                count = sum(1 for p in dogs if a * p[0] + b * p[1] + c == 0)
                d = round(abs(c) / (a ** 2 + b ** 2) ** 0.5, 2)
                if (count > mx) or (count == mx and d < dist):
                    mx = count
                    dist = d
    return dist


# Another Best Solution:
# https://py.checkio.org/mission/wild-dogs/publications/przemyslaw.daniel/python-3/9-liner-combine-all-pairs/?ordering=most_voted&filtering=all

def wild_dogs_(coords):
    from itertools import combinations
    result = []
    for (x0, y0), (x1, y1) in combinations(coords, 2):       
        A, B, C = y0-y1, x1-x0, y0*(x0-x1)-x0*(y0-y1)        
        distance = abs(C)/(A**2+B**2)**0.5                   
        result += [(distance, (1, B/A, C/A) if A else (A/B, 1, C/B))]
    distance, *_ = max(result, key=lambda x: (result.count(x), -x[0]))
    return round(distance, 2)



if __name__ == '__main__':
    print("Example:")
    print(wild_dogs([(7, 122), (8, 139), (9, 156), 
                     (10, 173), (11, 190), (-100, 1)]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156), 
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")