'https://py.checkio.org/en/mission/sum-of-distinct-cubes/share/6698d48e8f5d6b1a6716cad352452f92/'

'''
Positive integers can be broken down into sums of distinct cubes of positive integers, sometimes in multiple different ways. 
Your function should find and return the descending list of distinct cubes whose sum equals the given positive integer n. 
If it is impossible to express n as a sum of distinct cubes, return None.
'''

def sum_of_cubes(n: int) -> list[int] | None:
    
    def find_cubes_recursive(n, start):
        if n == 0:
            return []
        if n < 0 or start <= 0:
            return None
        
        for i in range(start, 0, -1):
            remaining = n - i**3
            result = find_cubes_recursive(remaining, i - 1)
            if result is not None:
                return [i] + result
        
        return None
    
    start = int(n**(1/3)) + 1
    result = find_cubes_recursive(n, start)
    if result:
        print(sorted(result, reverse=True))
        return sorted(result, reverse=True)
    else:
        return None


print("Example:")
#print(sum_of_cubes(1729))

# These "asserts" are used for self-checking
assert sum_of_cubes(1729) == [12, 1]
assert sum_of_cubes(8) == [2]
assert sum_of_cubes(11) == None

print("The mission is done! Click 'Check Solution' to earn rewards!")