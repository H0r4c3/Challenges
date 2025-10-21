'https://py.checkio.org/en/mission/championship-table/share/b58b239271cde10dadc68054fd524049/'

'''
Joana found an old booklet in the trophy room of the football club she supports, 
containing the results of all the championships the team has participated in. 
Each entry in the booklet gives five details of a championship: number of Games, Points, Wins (3 point/win), Draws (1 point/draw) and Losses. 
Some (one or two) of the numbers are illegible (-1), but they can be calculated using the legible numbers. 
Help Joana complete the information in the booklet.

    G = int()
    P = 3 * W + D
    W = (P - D) / 3
    D = P - 3 * W
    L = int()
    
    G = W + D + L
    P = int()
    W = G - D - L
    D = G - W - L
    L = G - W - D
    
    G = P + L - 2 * W
    P = 2 * W + G - L
    W = (P + L - G) / 2
    D = int()
    L = 2 * W + G - P
'''

Data = tuple[int, int, int, int, int]


def results(data: Data) -> Data:
    '''
    G = Games, P = Points, W = Wins, D = Draws, L = Losses
    '''
    G, P, W, D, L = data
    
    if G == -1:
        if P == -1:
            P = 3 * W + D
            G = W + D + L
        if W == -1:
            W = (P - D) / 3
            G = W + D + L
        if D == -1: 
            D = P - 3 * W
            G = W + D + L
        if L == -1:
            pass
        else:
            G = P + L - 2 * W
            
    if P == -1:
        if G == -1:
            G = W + D + L
            P = 3 * W + D
        if W == -1:
            W = G - D - L
            P = 3 * W + D
        if D == -1: 
            D = G - W - L
            P = 3 * W + D
        if L == -1:
            L = G - W - D
            P = 3 * W + D
        else:
            P = 3 * W + D
            
    if W == -1:
        if G == -1:
            pass
        if P == -1:
            pass
        if D == -1: 
            W = (P - G + L) / 2
            D = G - W - L
        if L == -1:
            W = (P - D) / 3
            L = G - W - D
        else:
            W = (P - D) / 3
        
    if D == -1:
        if G == -1:
            G = P + L - 2 * W
            D = P - 3 * W
        if P == -1:
            P = 2 * W + G - L
            D = P - 3 * W
        if W == -1: 
            W = (P + L - G) / 2
            D = P - 3 * W
        if L == -1:
            L = 2 * W + G - P
            D = G - W - L
        else:
            D = P - 3 * W
        
    if L == -1:
        if G == -1:
            pass
        if P == -1:
            pass
        if W == -1: 
            pass
        if D == -1:
            pass
        else:
            L = G - W - D
               
    result = list(map(int, (G, P, W, D, L)))
    print(result)
    G, P, W, D, L = result
    return G, P, W, D, L


print("Example:")
#print(results([10, 20, 6, 2, -1]))

# These "asserts" are used for self-checking
assert results((10, 20, 6, 2, -1)) == (10, 20, 6, 2, 2)
assert results((-1, 64, 18, 10, 10)) == (38, 64, 18, 10, 10)
assert results((-1, 47, 14, -1, 9)) == (28, 47, 14, 5, 9)
assert results((10, 20, -1, 2, -1)) == (10, 20, 6, 2, 2)
assert results((10, 20, -1, -1, 2)) == (10, 20, 6, 2, 2)

print("The mission is done! Click 'Check Solution' to earn rewards!")