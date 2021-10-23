
'https://www.pythonmorsels.com/exercises/v2/0ec0811f0d434499b4f77915a8de41d4/detail/'
'https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/submit/1/'

'''
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in 
the two given lists-of-lists added together.
'''

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
matrix3 = [[2, 3], [-3, 1]]
matrix_sum = list()


def add_matrixs(matrix1, matrix2):
    for i in range(len(matrix1)):
        matrix_sum.append([x + y for (x, y) in zip(matrix1[i], matrix2[i])])
            
    return matrix_sum

def add_multiple(*args):
    print(args)
    matrix_sum = list()
    for item in args:
        #for i in range(len(item[0])):
        matrix_sum.append([item[0] + item[1] for (item[0], item[1]) in zip(item[0], item[1])])
            
    return matrix_sum

def check_same_shape(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        raise ValueError("Given matrices are not the same size.")
        
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            raise ValueError("Given matrices are not the same size.")

check_same_shape(matrix1, matrix2)

#print(add_matrixs(matrix1, matrix2))

print(add_multiple(matrix1, matrix2, matrix3))