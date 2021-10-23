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

# S = [None]*10
# T = [None]*10
# Q = input()

# for i in range (int(Q)):
#     S[i] = input()
#     T[i] = input()
    
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pos = []

def shift(S, T):
    for i in range(len(S)):
        pos_S = alphabet.index(S[i])
        pos_T = alphabet.index(T[i])
        pos.append(abs(pos_S - pos_T))
        
    if len(set(pos)) == 1:
        result = pos[0]
    else:
        result = -1
        
    return result

S = 'ABC' 
T = 'DEF'
result = shift(S, T)
print(result)