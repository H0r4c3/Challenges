'https://py.checkio.org/en/mission/boolean-algebra/'

'''
In this mission you should implement some boolean operations:
- "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.
- "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
- "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. 
If x is true then the value of x → y is taken to be that of y. 
But if x is false then the value of y can be ignored; however the operation must return some truth value and there are only two choices, 
so the return value is the one that entails less, namely true.
- "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). 
It excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.
- "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value.
'''

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction": return x and y 
    if operation == "disjunction": return x or y
    if operation == "implication": return not x or y
    if operation == "exclusive":   return x ^ y
    if operation == "equivalence": return not(x ^ y)
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('All good! Go and check the mission.')