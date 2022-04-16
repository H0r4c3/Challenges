'https://py.checkio.org/en/mission/mono-captcha/'

'''
Your program should read the number shown in an image encoded as a binary matrix. Each digit can contain a wrong pixel, but no more than one for each digit. 
The space between digits is equal to one pixel (just think about "1" which is narrower than other letters, but has a width of 3 pixels).
'''
import numpy as np
from typing import List

FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")


def convert_string_to_arrays(FONT):
    '''
    Convert the FONT string into an array of 10 arrays, correspoding to 1,2,3,4,5,6,7,8,9,0 digits
    '''
    font_digits = FONT.replace('-', '0').replace('X', '1')
    font_list = [font_digits[i : i+41] for i in range(0, 200, 41)] # convert into a list of strings
    font_lists_digits = list(map(lambda x: list(map(int, x)), font_list)) # convert the strings in lists of 0s and 1s
    font_array = np.array(font_lists_digits)
    digits_arr = np.array([font_array[0:6, i:i+3] for i in range(1, 40, 4)]) # split in 10 small arrays, one array for every digit
    digits_list = digits_arr.tolist()[-1:] + digits_arr.tolist()[:-1] # move the '0' digit to the first place in the list
    digits_arr = np.array(digits_list)
    
    return digits_arr


def convert_image_into_numbers(image):
    '''
    Convert the image onto 3 arrays, each for each number
    '''
    arr_of_numbers = [[]]
    image_array = np.array(image)
    
    # first_number = image_array[0:6, 1:4]
    # second_number = image_array[0:6, 5:8]
    # third_number = image_array[0:6, 9:12]
    # forth_number = image_array[0:6, 9:12]
    
    for i in range(1, len(image[0]), 4):
        number = image_array[0:6, i:i+3]
        arr_of_numbers.append(number)

    return arr_of_numbers

def compare_arrays(image_number, font_number):
    '''
    Compare the array (from image) representing a number with 
    the array (from FONT) representing a number
    '''
    compare_array = image_number==font_number
    numbers_of_True = np.count_nonzero(compare_array)
    return numbers_of_True

def convert_to_digit(number, result_list):
    '''
    Decide what number represents the array from image comparing 
    the array from image with all the arrays from FONT
    '''
    digits_arr = convert_string_to_arrays(FONT)
    for i in range(10):
        result = compare_arrays(number, digits_arr[i])
        if result in [14, 15]:
            result_list.append(i)
    return result_list
    
    
  
def checkio(image: List[List[int]]) -> int:
    result_list = list()

    #first_number, second_number, third_number, forth_number = convert_image_into_numbers(image)
    arr_of_numbers = convert_image_into_numbers(image)
    
    for number in arr_of_numbers:
        result_list = convert_to_digit(number, result_list)
    
    result = int(''.join(map(str, result_list)))
    
    print(result)
    return result



# Best Solution: 
# https://py.checkio.org/mission/mono-captcha/publications/_Chico_/python-3/first/share/67ab239138c1b4edd6d404b082aec761/

def checkio_(image):

    tr = str.maketrans('-X', '01')
    font = [[int(f) for f in list(FONT[n * 41: n * 41 + 40].translate(tr))] for n in range(5)]
    result = ''
    for i in range(1, len(image[0]), 4):
        for j in range(1, len(font[0]), 4):
            dif = 0
            for k in range(len(font)):
                for m in range(3):
                    if image[k][i + m: i + m + 1] != font[k][j + m: j + m + 1]:
                        dif += 1
            if dif <= 1:
                num = j // 4 + 1
                result += str(num if num < 10 else 0)
                break
    
    return int(result)


if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"
    
    assert checkio([[0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0],
                    [0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0],
                    [0,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0],
                    [0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0],
                    [0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,1,0]]) == 1034
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
