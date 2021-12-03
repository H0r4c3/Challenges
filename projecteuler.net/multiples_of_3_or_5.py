'https://projecteuler.info/problem=1'

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''



def sum_of_multiples(n:int) -> int:
    sum_35 = 0
    
    for item in range(0, n):
        if (item % 3 == 0) or (item % 5 == 0):
            sum_35 += item
        
    return sum_35


if __name__ == "__main__":
    
    n = 1000
    print(sum_of_multiples(n))