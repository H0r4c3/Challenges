'https://py.checkio.org/en/mission/factorial-zeros/share/5266b84bac9a0e306e66034d9d0d110f/'

'''
Write a function that finds the number of zeros at the end of the decimal expansion of factorial n!. 
Because factorials grow very fast, it is not a good strategy to calculate n! and count the zeros.
'''

'''
To determine the number of trailing zeros in the decimal expansion of n!, we can utilize the properties of factorials 
rather than calculating the factorial directly. The key insight is to understand that trailing zeros are produced by the factors of 10 in the number. Since 
10 = 2*5, and there are generally more factors of 2 than 5 in factorials, the number of trailing zeros is determined by the number of times 5 is a factor 
in the numbers from 1 to n.
'''

def fact_zeros(n: int) -> int:
    count = 0
    
    while n > 4:
        count += n // 5
        n //= 5
    
    print(count)
    return count


# Best Solution: Recursion
# https://py.checkio.org/mission/factorial-zeros/publications/kdim/python-3/recursion/?ordering=most_voted&filtering=all

def fact_zeros_(n: int) -> int:
    return fact_zeros(n // 5) + n // 5 if n != 0 else 0


print("Example:")
#print(fact_zeros(2))

# These "asserts" are used for self-checking
assert fact_zeros(2) == 0
assert fact_zeros(5) == 1
assert fact_zeros(20) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")