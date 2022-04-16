'https://py.checkio.org/en/mission/stick-sawing/'

'''
The parts should have different lengths (no repeating). For example: 64 should divided at 15, 21, 28 , 
because 28, 36 is shorter and 1, 3, 15, 45 is not a consecutive fragment.

You are given a length of the stick (N). You should return the list of lengths (integers) for the parts in ascending order. 
If it's not possible and the problem does not have a solution, then you should return an empty list.

https://en.wikipedia.org/wiki/Triangular_number
The sequence of triangular numbers, starting with the 0th triangular number, is

0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666...

'''

# My First Solution

def calculate_triangular_numbers(n):
    triangular_numbers_list = [i * (i+1) // 2 for i in range(n) if i * (i+1) // 2 < n]
    
    return triangular_numbers_list 
    
def checkio_(number):
    
    triangular_numbers_list = calculate_triangular_numbers(number)
    print(triangular_numbers_list)
    
    i = 1
    j = 1
    sum = 0
    while i < len(triangular_numbers_list):
        sum += triangular_numbers_list[i]
        if sum == number:
            print(triangular_numbers_list[j:i+1])
            return triangular_numbers_list[j:i+1]
        elif sum < number:
            i += 1
        else:
            sum = 0
            j += 1
            i = j
    
    return []

# My Second Solution
def checkio(number):
    
    triangular_numbers_list = [i * (i+1) // 2 for i in range(number) if i * (i+1) // 2 < number]
    print(triangular_numbers_list)
    
    list_of_lists = [triangular_numbers_list[j : i+1] for j in range(1, len(triangular_numbers_list)) for i in range(j, len(triangular_numbers_list))]
    print(list_of_lists)
    
    results = [item for item in list_of_lists if sum(item) == number] 
    print(results)
    
    result = max(results, key=len) if results != [] else []
    print(result)
    
    return result
    

# Best Solution:
# https://py.checkio.org/mission/stick-sawing/publications/fed.kz/python-3/i-like-recursion/?ordering=most_voted&filtering=all

def checkio(num,a=1,b=0,l=[]):
    count=a
    while sum(l) < num:
        l += [b]
        a, b = a+1, b+a
    if sum(l)==num: return l
    if len(l)==1: return []
    return checkio(num, count+1, l[1], [])     
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
    print('Done!')