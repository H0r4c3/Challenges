'https://py.checkio.org/en/mission/sum-of-digits/'

'''
You are given an integer. 
If it consists of one digit, simply return its value. 
If it consists of two or more digits - add them until the number contains only one digit and return it.
'''

def sum_digits(num: int) -> int:
    
    num_list = list(str(num))
    print(f'num_list = {num_list}')
    
    if len(num_list) == 1:
        num = int(num_list[0])
        print(f'Final num = {num}')
    else:
        num = sum(map(int, num_list))
        print(f'num after sum = {num}')
        num = sum_digits(num)

    return(num)


# Best Solution:
# https://py.checkio.org/mission/sum-of-digits/publications/kdim/python-3/sum-and-recursion-one-line/?ordering=most_voted&filtering=all

def sum_digits(num: int) -> int:
    return num if num < 10 else sum_digits(sum(map(int, str(num))))


print("Example:")
#print(sum_digits(38))

assert sum_digits(38) == 2
assert sum_digits(0) == 0
assert sum_digits(10) == 1
assert sum_digits(132) == 6
assert sum_digits(232) == 7
assert sum_digits(811) == 1
assert sum_digits(702) == 9

print("The mission is done! Click 'Check Solution' to earn rewards!")