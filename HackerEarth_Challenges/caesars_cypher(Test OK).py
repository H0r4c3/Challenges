'hackerearth.com'

'''
Test - nr. 2 - Python (Easy)

Each letter is replaced by a letter some fixed number of positions down the alphabet.
For example, with a shift of 3, D would be replaced by G.

Input:
The first line of the input contains Q, denoting the number of queries.
The next Q lines contain two strings, S and T, consisting of only upper-case letters.

Output:
For each test-case, output a single non-negative integer denoting the minimum value of shift that was used to encrypt.

'''

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def shift(S, T):
    pos = list()
    for i in range(len(S)):
        pos_S = alphabet.index(S[i])
        pos_T = alphabet.index(T[i])
    
        if pos_T >= pos_S:
            encryption = pos_T - pos_S
            pos.append(encryption)
        elif pos_S > pos_T:
            encryption = 26 - pos_S + pos_T
            pos.append(encryption)
            
    
    if len(set(pos)) == 1:
        result = pos[0]
    else:
        result = -1
        
    return result


S = 'ABC'
T = 'DEF'
# S = 'AAA'
# T = 'PQR'
S = 'U'
T = 'R' # -> 23

result = shift(S, T)
print(result)



# Q = int(input())

# for _ in range(Q):
#     S = input()
#     T = input()
#     result = shift(S, T)
#     print(result)