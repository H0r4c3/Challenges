'https://www.codingame.com/evaluate/19711523?id=49129273b10ccefc864da38d66c7659e662376d'

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = 'AB'
s = 'Bd5'

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '01234567890'
for item in s:
    print(item)
    if item.isupper():
        ind = alphabet_U.find(item)
        print(ind)
        new_s = alphabet_U[:ind+1]
        print(new_s)
    if item.islower():
        ind = alphabet.find(item)
        new_s = alphabet[:ind+1]
        print(new_s)
    if item.isnumeric():
        ind = numbers.find(item)
        new_s = numbers[:ind+1]
        print(new_s)
        
