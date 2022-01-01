'https://py.checkio.org/en/mission/extremely-ugly/'

'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... shows the first 11 ugly numbers. By convention, 1 is included. 
Write a program to find and print the N’th ugly number. 
Same as previous task with a minor difference - input value limit is 1000000, and output is str.

Input: N, int.

Output: N'th Ugly Number, str.
'''

from functools import reduce

def extremely_ugly(n: int) -> str:
    p2, p3, p5 = 0, 0, 0
    uglynumber = [1]
    while len(uglynumber) < n:
        ugly2, ugly3, ugly5 = uglynumber[p2]*2, uglynumber[p3]*3, uglynumber[p5]*5
        next = min(ugly2, ugly3, ugly5)
        if next == ugly2: p2 += 1        # multiply each number
        if next == ugly3: p3 += 1        # only once by each
        if next == ugly5: p5 += 1        # of the three factors
        uglynumber += [next]
        
    return str(uglynumber[-1])




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


if __name__ == "__main__":
    print("Example:")
    print(extremely_ugly(4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert extremely_ugly(4) == "4"
    assert extremely_ugly(6) == "6"
    assert extremely_ugly(11) == "15"
    assert extremely_ugly(999) == "51018336"
    print("Extremely Ugly Numbers coding complete? Click 'Check' to earn cool rewards!")