'https://py.checkio.org/en/mission/stair-steps/'

'''
There is a staircase with N steps and two platforms; one at the beginning, the other at the end of the stairs. 
On each step a number is written (ranging from -100 to 100 with the exception of 0.) Zeros are written on both platforms. 
You start going up the stairs from the first platform, to reach the top on the second one. You can move either to the next step or to the next step plus one. 
You must find the best path to maximize the result of numbers on the stairs on your way up and return the final result.
'''

def checkio(numbers):
    previous = 0
    current = 0
    
    for number in numbers:
        previous, current = current, max(previous, current) + number
        
    result = max(previous, current)
    print(result)
    return result




# Best Solution
# https://py.checkio.org/mission/stair-steps/publications/StefanPochmann/python-3/short-simple-efficient-clear/?ordering=most_voted&filtering=all

def checkio_(numbers):
    a = b = 0
    for n in numbers:
        a, b = b, n + max(a, b)
    return max(a, b)

# Best Solution
# https://py.checkio.org/mission/stair-steps/publications/juestr/python-3/dynamic-programming/?ordering=most_voted&filtering=all

def checkio_(numbers):
    step1, step2 = 0, 0
    while numbers:
        step1, step2 = numbers.pop() + max(step1, step2), step1
    return max(step1, step2)



# Solution 1 NOK

def checkio_(numbers):
    #en = list(enumerate(numbers))
    #print(en)
    
    result = 0
    jump = 0
    print(numbers)
    for i in range(len(numbers)-1):
        print(i)
        if numbers[i] < 0 and numbers[i+1] < 0:
            if jump == 1:
                result += numbers[i+1]
                jump = 0
            else:    
                if numbers[i] >= numbers[i+1]:
                    result += numbers[i]
                    print(f'result1 after adding {numbers[i]} = {result}')
                    jump = 1
                else:
                    result += numbers[i+1]
                    jump = 1
                    print(f'result2 after JUMP and adding {numbers[i+1]} = {result}')
        elif numbers[i] > 0 and numbers[i+1] < 0:
            result += numbers[i]
            jump = 1
            print(f'result3 after adding {numbers[i]} = {result}')   
        elif numbers[i] < 0 and numbers[i+1] > 0:
            result += numbers[i+1]
            jump = 0
            print(f'result4 after JUMP and adding {numbers[i+1]} = {result}')
        else:
            result += numbers[i]
            jump = 0
            print(f'result5 after adding {numbers[i]} = {result}')
    
    print(f'result = {result} \n')
    return result


# Solution 2 NOK
from itertools import pairwise
import numbers

def checkio_(numbers):
    pairs = pairwise(numbers)
    pairs = [list(item) for item in pairs]
    print(pairs)
    
    result = 0
    for item in pairs:
        if item[0] < 0 and item[1] < 0:
            idx = pairs.index(item)
            print(idx)
            result += max(item[0], item[1])
            if idx == len(pairs) - 1: return result
            if max(item[0], item[1]) == item[1]:
                pairs[idx+1][0] = float('-inf')
                print(pairs)
        elif item[0] > 0 and item[1] > 0: 
            result = item[0] + item[1]
        else:
            idx = pairs.index(item)
            print(idx)
            result += max(item[0], item[1])
            if idx == len(pairs) - 1: return result
            if max(item[0], item[1]) == item[1]:
                pairs[idx+1][0] = float('-inf')
                print(pairs)
    
    print(result)
    return result


# Solution 3 NOK

from functools import reduce

def calculation(a, b):
    if a < 0 and b < 0:
        return max(a, b)
    elif a > 0 and b > 0:
        return a + b
    else:
        return a + b

def checkio_(numbers):
    print(numbers)
    result = reduce(calculation, numbers)
    
    print(result)
    return result



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, 'Third'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, 'Second'
    assert checkio([5,4,3,-99,2,-20]) == 14
    
    print('All ok')