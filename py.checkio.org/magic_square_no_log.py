

import numpy as np
from itertools import permutations

def find_dimensions(data_arr):
    '''
    3x3: range(10), sum = n*(n**2 + 1)/2 = 15
    4x4: range(17), sum = 34
    5x5: range(26), sum = 65
    '''
    n = data_arr.shape[0]
    numbers = list(range(1, data_arr.size + 1)) # possible numbers in the magic square
    total = int(n * (n**2 + 1) / 2) # sum
    size = len(data_arr[0]) # dimension of the magic square
    
    return numbers, total, size
    

def total_zeros(data_arr):
    number_of_zeros = data_arr.size - np.count_nonzero(data_arr)
    zeros_coords = np.where(data_arr==0)
    list_of_zero_coords = list(zip(zeros_coords[0], zeros_coords[1]))
    
    return number_of_zeros, list_of_zero_coords


def possible_digits(data_arr, numbers):
    digits_in_square = [list(d) for d in data_arr]
    digits_in_square_flat = [item for sublist in digits_in_square for item in sublist]
    digits_not_in_square = [d for d in numbers if d not in digits_in_square_flat]
    return digits_in_square, digits_not_in_square


def replace_zeros(data_arr, list_of_zero_coords, digits_not_in_square):
    data_arr_new = data_arr.copy()
    i = 0
    for coords in list_of_zero_coords:
        data_arr_new[coords] = digits_not_in_square[i]
        i += 1
    
    return data_arr_new


def verify_magic_square(data_arr_for_check, total):
    # check sum on rows
    sum_rows = np.sum(data_arr_for_check, axis=0)
    if any([item != total for item in sum_rows]):
        return False
    
    # check sum on columns
    sum_cols = np.sum(data_arr_for_check, axis=1)
    if any([item != total for item in sum_cols]):
        return False
    
    # check sum on diagonals
    diag1 = np.diag(data_arr_for_check, 0)
    diag2 = np.fliplr(data_arr_for_check).diagonal()
    sum_diag1 = sum(diag1)
    sum_diag2 = sum(diag2)
    if sum_diag1 != total:
        return False
    if sum_diag2 != total:
        return False

    return True


def checkio(data):
    data_arr = np.array(data)
    
    numbers, total, size = find_dimensions(data_arr)
    number_of_zeros, list_of_zero_coords = total_zeros(data_arr)
    
    digits_in_square, digits_not_in_square = possible_digits(data_arr, numbers)
    
    # all permutations of digits_not_in_square
    digits_not_in_square_All = permutations(digits_not_in_square)
    
    for digits_not_in_square in digits_not_in_square_All:
        data_arr_new = replace_zeros(data_arr, list_of_zero_coords, digits_not_in_square)
        check = verify_magic_square(data_arr_new, total)
        if check:
            print(f'data_arr_new OK = \n{data_arr_new}')
            return data_arr_new
        
    print('NO Solution!!!')
    
    
    
    
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

    # assert check_solution(checkio, [[0, 0, 0], [0, 5, 0], [0, 0, 0]]), "2nd example"

    # assert check_solution(checkio, [[1, 15, 14, 4], [12, 0, 0, 9], [8, 0, 0, 5], [13, 3, 2, 16]]), "3rd example"
    
    # assert check_solution(checkio, [[1,15,14,4],[12,0,0,9],[8,0,0,5],[13,3,2,16]])
    
    assert check_solution (checkio, [[3,7,14,16,25],[11,0,0,0,9],[22,0,0,0,18],[10,0,0,0,1],[19,21,5,8,12]])
    
    print('Done!!!')