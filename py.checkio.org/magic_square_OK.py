'https://py.checkio.org/en/mission/magic-square/'

'''
You have been given an incomplete magic square (with a size from 3 to 5). With your coding skills, you must finish the square.
'''

# Best Solution: 
# https://py.checkio.org/mission/magic-square/publications/veky/python-3/filter-all/share/0a35e14a5e4c8ef81cd7f9f55a18b51f/

def checkio_(s):
    n,a=len(s),sum(s,[])
    if all(sum(t)*2==n+n**3 for t in filter(all,s+
        list(zip(*s))+[a[::n+1],a[::n-1][1:-1]])):
        try: i,j=divmod(a.index(0),n)
        except ValueError: return s
        for r in set(range(1,n*n+1)).difference(a):
            s[i][j]=r
            t=checkio(s)
            if t: return t
        s[i][j]=0
        
        
# Solution with explanations      
def checkio(s):
    # The dimension of the square
    n = len(s)
    # A flattened version
    a = sum(s,[])
    # Check if a row, column or diagonal has the right sum
    def right_sum(t):
        return sum(t) * 2 == n + n**3
    # Checks if all rows, columns and diagonals that do not contain zeroes have the right sum
    def good():
        rows = s
        columns = list(zip(*s))
        diagonals = [a[::n+1], a[::n-1][1:-1]]
        full_already = filter(all, rows + columns + diagonals)
        return all(right_sum(t) for t in full_already)
    # Now, if it's good so far, solve the rest recursively
    if good():
        try:
            i, j = divmod(a.index(0), n)    # first unknown cell
        except ValueError:
            return s                        # return if none
        # Try all remaining numbers for the unknown cell
        remaining = set(range(1, n*n+1)).difference(a)
        for r in remaining:
            s[i][j] = r
            t = checkio(s)
            if t: return t
        # Backtrack, if no solution was found
        s[i][j] = 0
        

if __name__ == "__main__":
    # This part is using only for self-testing.
    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        # check sizes
        N = len(result)
        if len(result) == N:
            for row in result:
                if len(row) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
        # check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for row in result:
            if sum(row) != line_sum:
                print(MS_ERROR)
                return False
        for col in zip(*result):
            if sum(col) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        # check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
        # check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True

    
    # assert check_solution(checkio, [[2, 7, 6], [9, 5, 1], [4, 3, 0]]), "1st example"

    #assert check_solution(checkio, [[0, 0, 0], [0, 5, 0], [0, 0, 0]]), "2nd example"

    # assert check_solution(checkio, [[1, 15, 14, 4], [12, 0, 0, 9], [8, 0, 0, 5], [13, 3, 2, 16]]), "3rd example"
    
    # assert check_solution(checkio, [[1,15,14,4],[12,0,0,9],[8,0,0,5],[13,3,2,16]])
    
    assert check_solution (checkio, [[3,7,14,16,25],[11,0,0,0,9],[22,0,0,0,18],[10,0,0,0,1],[19,21,5,8,12]])
    
    print('Done!!!')