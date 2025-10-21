'https://py.checkio.org/en/mission/perfect-number-checking/'

'''
A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

For example, 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and their sum is 28.
'''

def is_perfect_(n: int) -> bool:
    def find_divisors(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return divisors
    
    divisors = find_divisors(n)
    
    if sum(divisors) == n:
        return True
    else:
        return False
    
    
# Best Solution: 
# https://py.checkio.org/mission/perfect-number-checking/publications/freeman_lex/python-3/forth/?ordering=most_voted&filtering=all


def is_perfect(n: int) -> bool:
    
    divisors = filter(lambda x: n % x == 0, range(1, n))
    
    return sum(divisors) == n


print("Example:")
print(is_perfect(3))

# These "asserts" are used for self-checking
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False
assert is_perfect(496) == True
assert is_perfect(30) == False
assert is_perfect(8128) == True
assert is_perfect(100) == False
assert is_perfect(500) == False
assert is_perfect(1000) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")