'https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/caesars-cipher-1/'

'''
Caesar's Cipher is a very famous encryption technique used in cryptography. It is a type of substitution cipher in which each letter in 
the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, D would be 
replaced by G, E would become H, X would become A and so on.
Encryption of a letter X by a shift K can be described mathematically as (X + K) % 26.
Given a plaintext and it's corresponding ciphertext, output the minimum non-negative value of shift that was used to encrypt the plaintext or 
else output -1 if it is not possible to obtain the given ciphertext from the given plaintext using Caesar's Cipher technique.
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