'https://py.checkio.org/en/mission/compass-map-and-spyglass/'

'''
Your task is to count the sum of the number of steps required to pick up all 3 items - ('C' - compass), ('M' - map), ('S' - spyglass) from your starting position. 
So the result will be the sum of distance from Y to C, from Y to M and from Y to S (not Y-C-M-S).
Note that you can walk in 8 directions - left, right, up, down and sideways (on the diagonal in any direction). Your starting position is 'Y'.
'''

def navigation(seaside):
    for row in range(len(seaside)):
        for column in range(len(seaside[row])):
            match(seaside[row][column]):
                case 'Y':
                    coords_Y = (row, column)
                case 'C':
                    coords_C = (row, column)
                case 'M':
                    coords_M = (row, column)
                case 'S':
                    coords_S = (row, column)   
        
    steps_C = max((abs(coords_Y[0] - coords_C[0])), (abs(coords_Y[1] - coords_C[1])))
    steps_M = max((abs(coords_Y[0] - coords_M[0])), (abs(coords_Y[1] - coords_M[1])))
    steps_S = max((abs(coords_Y[0] - coords_S[0])), (abs(coords_Y[1] - coords_S[1])))
    steps = steps_C + steps_M + steps_S
        
    print(steps)    
    return steps




# Best Solution:
# https://py.checkio.org/mission/compass-map-and-spyglass/publications/kuzdras/python-3/first/share/fcf844b4a8a94c602779d9bbc659eb99/


def navigation_(seaside):
    for row in range(len(seaside)):
        for column in range(len(seaside[row])):
            if seaside[row][column] == "Y":
                y = [row, column]
            elif seaside[row][column] == "C":
                c = [row, column]
            elif seaside[row][column] == "M":
                m = [row, column]
            elif seaside[row][column] == "S":
                s = [row, column]
    route = 0
    for a in [c, m, s]:
        route += max((abs(y[0] - a[0])), (abs(y[1] - a[1])))    
    return route



# Another Best Solution: 
# https://py.checkio.org/mission/compass-map-and-spyglass/publications/flpo/python-3/x0-y0-positionspopy/?ordering=most_voted&filtering=all

def navigation_(seaside):
    positions = {cell: (i, j) for i, row in enumerate(seaside) for j, cell in enumerate(row) if cell}
    x0, y0 = positions.pop('Y')
    return sum(max(abs(x0 - x1), abs(y0 - y1)) for x1, y1 in positions.values())



if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")