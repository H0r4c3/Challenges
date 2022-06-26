'https://py.checkio.org/en/mission/graphical-key/'

'''
Your task is to write a function that accepts a set of digits (a two-dimensional array) as an argument, 
and then returns the sum of the digits on the direction from the upper-left corner to the lower right so that the sum is maximum. 
At the same time, you can visit no more than N points, taking into account the first and the last one. 
You can move in any of the 8 directions (horizontally, vertically and diagonally).
'''
all_paths = list()

# Solution NOK !!!!!!!!!
def findPaths(matrix, m, n):
    path = [0 for _ in range(m+n-1)]
    all_paths_zero = findPathsUtil(matrix, m, n, 0, 0, path, 0)
    print(f'all_paths_zero = {all_paths_zero}')
    
    return all_paths_zero

     
def findPathsUtil(matrix, m, n, i, j, path, index):
    global all_paths
    
    # if we reach the bottom of maze, we can only move right
    if i == m-1:
        for k in range(j, n):
            #path.append(maze[i][k])
            path[index + k - j] = matrix[i][k]
        # if we hit this block, it means one path is completed.
        # Add it to paths list and print
        print(f'path = {path}')
        print(sum(path))
        all_paths.append(path)
        #print(all_paths)
        return all_paths
    
    # if we reach to the right most corner, we can only move down
    if j == n - 1:
        for k in range(i, m):
            path[index + k - i] = matrix[k][j]
          #path.append(maze[j][k])
        # if we hit this block, it means one path is completed.
        # Add it to paths list and print
        print(f'path = {path}')
        print(sum(path))
        all_paths.append(path)
        #print(all_paths)
        return all_paths
     
    # add current element to the path list
    #path.append(maze[i][j])
    path[index] = matrix[i][j]
     
    # move down in y direction and call findPathsUtil recursively
    findPathsUtil(matrix, m, n, i+1, j, path, index+1)
     
    # move down in y direction and call findPathsUtil recursively
    findPathsUtil(matrix, m, n, i, j+1, path, index+1)
    

def g_key(grid, length_of_path):
    m = len(grid)
    n = len(grid[0])
    
    all_paths_zero = findPaths(grid, m, n)
    print(all_paths_zero)
    
    result_paths = [item for item in all_paths_zero if len(item) == length_of_path]
    #print(result_paths)
    print(len(result_paths))
    
    result = max(map(sum, result_paths))
    print(result)
    
    return result
    
    






if __name__ == '__main__':
    print("Example:")
    # print(g_key([[1, 6, 7, 2, 4],
    #              [0, 4, 9, 5, 3],
    #              [7, 2, 5, 1, 4],
    #              [3, 3, 2, 2, 9],
    #              [2, 6, 1, 4, 0]], 9))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert g_key([[1, 6, 7, 2, 4],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 0]], 9) == 46 # 1, 6, 7, 9, 5, 5, 4, 9, 0

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