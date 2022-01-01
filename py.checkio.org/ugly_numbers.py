'https://py.checkio.org/en/mission/ugly-numbers/'

'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... shows the first 11 ugly numbers. 
By convention, 1 is included. Write a program to find and print the N’th ugly number
'''
from functools import reduce

# execution time is too long!!!
def ugly_number_H(N: int) -> int:
    
    def is_ugly_number(n):
        if n == 0:
            return False
            
        for i in [2, 3, 5]:
            #print(f'i = {i}')
            while n % i == 0:
                n = n/i
                #print(f'n = {n}')
        
        if n == 1:
            return True
        else:       
            return False

    # ugly_list = list()
    
    # for i in range(N**2 + 1):
    #     if is_ugly_number(i):
    #         ugly_list.append(i)
    #         if len(ugly_list) == N:
    #             print(ugly_list)
    #             return ugly_list[-1]
            
    def nthUgly(N):
        i = 1
        count = 1
        while N > count:
            i += 1
            if is_ugly_number(i):
                count += 1
                #print(count)
        return i
    
    return nthUgly(N)


def ugly_number(n: int) -> int:
    p2, p3, p5 = 0, 0, 0
    uglynumber = [1]
    while len(uglynumber) < n:
        ugly2, ugly3, ugly5 = uglynumber[p2]*2, uglynumber[p3]*3, uglynumber[p5]*5
        next = min(ugly2, ugly3, ugly5)
        if next == ugly2: p2 += 1        # multiply each number
        if next == ugly3: p3 += 1        # only once by each
        if next == ugly5: p5 += 1        # of the three factors
        uglynumber += [next]
        
    return uglynumber[-1]




'''
https://stackoverflow.com/questions/4600048/n%e1%b5%97%ca%b0-ugly-number

Here is another O(n) approach (Python solution) based on the idea of merging three sorted lists. 
The challenge is to find the next ugly number in increasing order. For example, we know the first seven ugly numbers are [1,2,3,4,5,6,8]. 
The ugly numbers are actually from the following three lists:

list 1: 1*2, 2*2, 3*2, 4*2, 5*2, 6*2, 8*2 ...     ( multiply each ugly number by 2 )
list 2: 1*3, 2*3, 3*3, 4*3, 5*3, 6*3, 8*3 ...     ( multiply each ugly number by 3 )
list 3: 1*5, 2*5, 3*5, 4*5, 5*5, 6*5, 8*5 ...     ( multiply each ugly number by 5 )

So the nth ugly number is the nth number of the list merged from the three lists above:

1, 1*2, 1*3, 2*2, 1*5, 2*3 ...
'''
def ugly_number(n):
    p2, p3, p5 = 0, 0, 0
    uglynumber = [1]
    while len(uglynumber) < n:
        ugly2, ugly3, ugly5 = uglynumber[p2]*2, uglynumber[p3]*3, uglynumber[p5]*5
        next = min(ugly2, ugly3, ugly5)
        if next == ugly2: p2 += 1        # multiply each number
        if next == ugly3: p3 += 1        # only once by each
        if next == ugly5: p5 += 1        # of the three factors
        uglynumber += [next]
        #print(uglynumber)
    return uglynumber[-1]
    
                

if __name__ == "__main__":
    print("Example:")
    print(ugly_number(4))
    print(ugly_number(29))
    print(ugly_number(84)) # -> 960
    print(ugly_number(1))
    print(ugly_number(313)) # -> 100000
    print(ugly_number(978))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ugly_number(4) == 4
    assert ugly_number(6) == 6
    assert ugly_number(11) == 15
    assert ugly_number(84) == 960
    assert ugly_number(313) == 100000, 'Jackpot!'