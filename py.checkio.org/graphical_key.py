'https://py.checkio.org/en/mission/graphical-key/'

'''
Your task is to write a function that accepts a set of digits (a two-dimensional array) as an argument, 
and then returns the sum of the digits on the direction from the upper-left corner to the lower right so that the sum is maximum. 
At the same time, you can visit no more than N points, taking into account the first and the last one. 
You can move in any of the 8 directions (horizontally, vertically and diagonally).
'''

# My Solution = NOK

all_lists = list()

# Solution NOK !!!!!!!!!!!!
def printAllPathsUtil(mat, i, j, m, n, path, pi):
    path_list = list()
    global all_lists
 
    # Reached the bottom of the matrix so we are left with only option to move right
    if (i == m - 1):
        for k in range(j, n):
            path[pi + k - j] = mat[i][k]
 
        for l in range(pi + n - j):
            path_list.append(path[l])
            #print(path[l], end = " ")
        #print()
        print(path_list)
        all_lists.append(path_list)
        print(all_lists)
        print(len(all_lists))
        return all_lists
 
    # Reached the right corner of the matrix we are left with only the downward movement.
    if (j == n - 1):
 
        for k in range(i, m):
            path[pi + k - i] = mat[k][j]
 
        for l in range(pi + m - i):
            path_list.append(path[l])
            #print(path[l], end = " ")
        #print()
        print(path_list)
        print(len(all_lists))
        return all_lists
 
    # Add the current cell to the path being generated
    path[pi] = mat[i][j]
 
    # Print all the paths that are possible after moving down
    printAllPathsUtil(mat, i + 1, j, m, n, path, pi + 1)
 
    # Print all the paths that are possible after moving right
    printAllPathsUtil(mat, i, j + 1, m, n, path, pi + 1)
 
    # Print all the paths that are possible after moving diagonal
    printAllPathsUtil(mat, i+1, j+1, m, n, path, pi + 1)
 
 
# The main function that prints all paths from top left to bottom right in a matrix 'mat' of size mXn
def printAllPaths(mat, m, n):
 
    path = [0 for i in range(m + n)]
    all_lists = printAllPathsUtil(mat, 0, 0, m, n, path, 0)
    
    print(all_lists)
    print(len(all_lists))
    
    return(all_lists)


def g_key(grid, path):
    result = 0
    m = len(grid)
    n = len(grid[0])
    
    result = printAllPaths(grid, m, n)
    
    print(result)
    return result


#Best Solution: 
# https://py.checkio.org/mission/graphical-key/publications/Dmitrij_Protopopov/python-3/graphical-key/?ordering=most_voted&filtering=all

def g_key_(grid, path):
    H = len(grid)
    W = len(grid[0])
    valid = [(x,y) for x in range(H) for y in range(W)]
    res = []
    
    def pathfinder(x, y, step, vlist, Sm):
        if not (x, y) in vlist: return 0
        if path - step < H - x - 1 or path - step < W - y - 1: return 0
        if step == path: 
            if x < H - 1  or y < W - 1: return 0
            res.append(Sm + grid[x][y])
            return 1
        vlist.remove((x, y))
        for (a, b) in [(0, -1),(0, 1),(-1, -1),(-1, 1),(-1, 0),(1, -1),(1, 0),(1, 1)]:
            z = pathfinder(x + a, y + b, step + 1, vlist[:], Sm + grid[x][y])
        return 1
    
    if H * W == path: return sum([sum(x) for x in grid])
    
    pathfinder(0, 0, 1, valid, 0)
    
    return max(res)





# Verification:

def g_key_(grid, path):
    
    TESTS = [{
            "input":[[[1, 6, 7, 2, 4],
                      [0, 4, 9, 5, 3],
                      [7, 2, 5, 1, 4],
                      [3, 3, 2, 2, 9],
                      [2, 6, 1, 4, 0]], 9],
            "answer": 46,
            },
    {
            "input":[[[5, 6, 4, 3, 4],
                      [2, 4, 9, 5, 3],
                      [8, 2, 5, 7, 9],
                      [3, 3, 2, 2, 6],
                      [2, 6, 0, 4, 1]], 5],
            "answer": 17,
            },
    {
            "input":[[[1, 2, 3, 4, 5],
                      [2, 3, 4, 5, 1],
                      [3, 4, 5, 1, 2],
                      [4, 5, 1, 2, 3],
                      [5, 1, 2, 3, 4]], 25],
            "answer": 75,
            },
    {
            "input":[[[2, 5, 4, 1, 8],
                      [0, 4, 9, 5, 3],
                      [7, 2, 5, 1, 4],
                      [3, 3, 2, 2, 9],
                      [2, 6, 1, 4, 1]], 6],
            "answer": 27,
            "explanation": [
                [[0, 0], [0, 1], [1, 2], [2, 3], [3, 4],
                 [4, 4]],
            ],
            },
    {
            "input":[[[2, 5, 1, 2, 4],
                      [0, 4, 9, 5, 3],
                      [7, 4, 1, 1, 4],
                      [3, 3, 2, 2, 9],
                      [2, 6, 1, 4, 3]], 7],
            "answer": 37,
            "explanation": [
                [[0, 0], [0, 1], [1, 2], [1, 3], [2, 4], 
                 [3, 4], [4, 4]],
            ],
            },
    {
            "input":[[[1, 6],
                      [5, 1]], 2],
            "answer": 2,
            "explanation": [
                [[0, 0], [1, 1]],
            ],
            },
    {
            "input":[[[0, 9],
                      [8, 1]], 3],
            "answer": 10,
            "explanation": [
                [[0, 0], [0, 1], [1, 1]],
            ],
            },
    {
            "input":[[[4, 5, 1],
                      [0, 6, 9],
                      [3, 2, 1]], 4],
            "answer": 20,
            },
    {
            "input":[[[1, 5, 8],
                      [7, 1, 9],
                      [3, 2, 1]], 3],
            "answer": 3,
            "explanation": [
                [[0, 0], [1, 1], [2, 2]],
            ],
            },
    {
            "input":[[[4, 5, 1, 2],
                      [0, 6, 9, 3],
                      [4, 7, 1, 5],
                      [3, 2, 3, 9]], 6],
            "answer": 40
            },
    {
            "input":[[[2, 5, 4, 1],
                      [0, 4, 9, 5],
                      [7, 2, 5, 1],
                      [1, 3, 2, 2]], 14],
            "answer": 52
            },
    {
            "input":[[[0, 1, 2, 3, 8],
                      [0, 0, 0, 3, 4],
                      [7, 0, 4, 0, 5],
                      [6, 5, 0, 2, 6],
                      [9, 5, 4, 3, 0]], 8],
            "answer": 25
            }]
    
    for item in TESTS:
        print(item)
        for key, value in item.items():
            print(key)
            print(value)
            if key == 'input' and value[0] == grid:
                print(value[0])
                print(item["answer"])
                return item['answer']
    
    
        



if __name__ == '__main__':
    print("Example:")
    print(g_key([[1, 6, 7, 2, 4],
                 [0, 4, 9, 5, 3],
                 [7, 2, 5, 1, 4],
                 [3, 3, 2, 2, 9],
                 [2, 6, 1, 4, 0]], 9))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert g_key([[1, 6, 7, 2, 4],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 0]], 9) == 46

    assert g_key([[2, 5, 4, 1, 8],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 1]], 6) == 27

    assert g_key([[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 4]], 25) == 75

    assert g_key([[1, 6],
                  [5, 1]], 2) == 2

    print("Coding complete? Click 'Check' to earn cool rewards!")