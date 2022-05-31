'https://py.checkio.org/en/mission/graphical-key/'

'''
Your task is to write a function that accepts a set of digits (a two-dimensional array) as an argument, 
and then returns the sum of the digits on the direction from the upper-left corner to the lower right so that the sum is maximum. 
At the same time, you can visit no more than N points, taking into account the first and the last one. 
You can move in any of the 8 directions (horizontally, vertically and diagonally).
'''
list_of_paths = list()

def allPathsUtil(mat, i, j, m, n, path, pi):
    path_list = list()
    global list_of_paths
    
 
    # Reached the bottom of the matrix, so we are left with only option to move right
    if (i == m - 1):
        for k in range(j, n):
            path[pi + k - j] = mat[i][k]
 
        for l in range(pi + n - j):
            path_list.append(path[l])
            #print(path[l], end = " ")
        #print()
        list_of_paths.append(path_list)
        print(list_of_paths)
        return list_of_paths
 
    # Reached the right corner of the matrix, we are left with only the downward movement.
    if (j == n - 1):
 
        for k in range(i, m):
            path[pi + k - i] = mat[k][j]
 
        for l in range(pi + m - i):
            path_list.append(path[l])
            #print(path[l], end = " ")
        #print()
        list_of_paths.append(path_list)
        print(list_of_paths)
        return list_of_paths
 
    # Add the current cell to the path being generated
    path[pi] = mat[i][j]
 
    # Print all the paths that are possible after moving down
    allPathsUtil(mat, i + 1, j, m, n, path, pi + 1)
 
    # Print all the paths that are possible after moving right
    allPathsUtil(mat, i, j + 1, m, n, path, pi + 1)
 
    # Print all the paths that are possible after moving diagonal
    allPathsUtil(mat, i+1, j+1, m, n, path, pi + 1)
 
 
def allPaths(mat, m, n):
 
    path = [0 for i in range(m + n)]

    path_list = allPathsUtil(mat, 0, 0, m, n, path, 0)
    print(path_list)
    
    return path_list
    

def g_key(grid, length_of_path):
    m = len(grid)
    n = len(grid[0])
    
    
    path_list = allPaths(grid, m, n)
    print(path_list)
    
    
    return 


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