'https://py.checkio.org/en/mission/magic-square/'

'''
You have been given an incomplete magic square (with a size from 3 to 5). With your coding skills, you must finish the square.
'''
import numpy as np

def find_dimensions(data_arr):
    '''
    3x3: range(10), sum = n*(n**2 + 1)/2 = 15
    4x4: range(17), sum = 34
    5x5: range(26), sum = 65
    '''
    n = data_arr.shape[0]
    numbers = list(range(1, data_arr.size + 1))
    total = int(n * (n**2 + 1) / 2)
    size = len(data_arr[0])
    
    return numbers, total, size
    

def total_zeros(data_arr):
    number_of_zeros = data_arr.size - np.count_nonzero(data_arr)
    return number_of_zeros


def possible_digits(data_arr, numbers):
    digits_in_square = [list(d) for d in data_arr]
    print(digits_in_square)
    digits_not_in_square = [d for d in numbers if d not in digits_in_square]
    return digits_not_in_square
    

def solving_system_of_equations(a, b):
    '''
    https://stackabuse.com/solving-systems-of-linear-equations-with-pythons-numpy/
    solution = np.linalg.solve(a, b)
    
    4x + 3y + 2z = 25
    -2x + 2y + 3z = -10
    3x -5y + 2z = -4
    '''

    #a = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
    a = np.array(a)
    #b = np.array([25, -10, -4])
    b = np.array(b)
    solution = np.linalg.solve(a, b)
    
    return solution

def check_magic_square(data_arr_for_check, total, size):
    # check sum on rows
    sum_rows = np.sum(data_arr_for_check, axis=0)
    if any(sum_rows) != total:
        print(f'Sum {sum_rows} on rows NOK!')
        return False
    
    # check sum on columns
    sum_cols = np.sum(data_arr_for_check, axis=1)
    if any(sum_cols) != total:
        print(f'Sum {sum_cols} on cols NOK!')
        return False
    
    # check sum on diagonals
    sum_diag1 = np.diag(data_arr_for_check)
    sum_diag2 = np.diag(data_arr_for_check)

    
    return True

def checkio(data):
    data_arr = np.array(data)
    print(data_arr)
    
    numbers, total, size = find_dimensions(data_arr)
    print(numbers, total, size)
    
    number_zeros = total_zeros(data_arr)
    print(f'number_of_zeros = {number_zeros}')
    
    digits_not_in_square = possible_digits(data_arr, numbers)
    print(digits_not_in_square)
    
    check = check_magic_square(data_arr, total, size)
    print(check)
    
    result = data_arr
    print(result)
    return result




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

    #assert check_solution(checkio, [[0, 0, 0], [0, 5, 0], [0, 0, 0]]), "2nd example"
    
    assert check_solution(checkio, [[2, 7, 6], [9, 5, 1], [4, 3, 0]]), "1st example"

    assert check_solution(checkio, [[0, 0, 0], [0, 5, 0], [0, 0, 0]]), "2nd example"

    assert check_solution(
        checkio, [[1, 15, 14, 4], [12, 0, 0, 9], [8, 0, 0, 5], [13, 3, 2, 16]]
    ), "3rd example"