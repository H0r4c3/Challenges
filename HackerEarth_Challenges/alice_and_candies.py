'https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/lola-and-candies-36b57b1b/'

'''
Alice loves candies, so she went into a candy shop. Now the shopkeeper sells candies in packets and all packets 
contain an odd number of candies (1, 3, 5, 7.....). Alice wants exactly  candies but she also loves patterns so she 
decided to buy candies only if the number of candies in the packets is consecutive and distinct (means she cannot buy the 
same candy packet more than once) and the sum of all the candies in those packets is exactly .

Alice has an infinite amount of money and the shopkeeper also has infinite amount candy packets, so Alice wonders how 
many different sets of candy packets she can buy.

Find the number of different sets of candy packets that Alice can buy.
'''

#N = input()


def number_of_different_sets_of_candy_packets_HORACE(N):
    
    if N == 1:
        return 1
    elif N == 2:
        return 0
        
    M = int((N+1)/2)
        
    all_odd = list(range(1, M+1, 2)) # 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23
    
    if N % 2 != 0:
        result = 1
    else:
        result = 0
    
    suma = 0   
    i = 0
    start = 0
    
    while i < len(all_odd):
        
        print(f'suma = {suma} + {all_odd[i]}')
        suma = suma + all_odd[i]
        
        if suma == N:
            print(f'suma={suma}={N}')
            result = result + 1
            print(f'!!!!!!!!!!!!!!result = {result}')
            suma = all_odd[i]
            print(f'new suma = {all_odd[i]}')
            start = i
            i = i + 1
        elif suma > N:
            print(f'suma={suma}>{N}')
            start = start + 1
            suma = 0
            i = start + 1
            print(f'new suma = {all_odd[i]}')
        else: # suma < N
            print(f'suma={suma}<{N} i={i} all_odd[i]={all_odd[i]}')
            i = i + 1
            
    return result


def number_of_different_sets_of_candy_packets_HORACE2(N):
    if N == 1:
        return 1
    elif N == 2:
        return 0
        
    # 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23
    
    if N % 2 != 0:
        result = 1
    else:
        result = 0
    
    suma = 0   
    i = 3
    start = 3
    M = int((N+1)//2)
    
    while i < M and i % 2 != 0:
        suma = suma + i
        print(f'suma = {suma}')
        
        if suma == N:
            result = result + 1
            print(f'result = {result}')
            suma = i
            start = i
            i = i + 2
        elif suma > N:
            start = start + 2
            print(f'start = {start}')
            suma = 0
            i = start
        else: # suma < N
            i = i + 2
            
    return result
from functools import reduce
def number_of_different_sets_of_candy_packets_OK(N):
    # 1 + 3 + 5 + ... + n = n**2
    
    k = list(reduce(list.__add__, ([i, N//i] for i in range(1, int(N**0.5) + 1) if N % i == 0)))

    count=0

    for a in list(range(len(k)-1))[::2]:
        if (k[a]+k[a+1])%2==0:
            count=count+1

    return count
            

N = 45
#N = 8
result = number_of_different_sets_of_candy_packets_OK(N)
print(result)