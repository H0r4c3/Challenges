'https://www.hackerrank.com/challenges/permutation-equation/problem?h_r=next-challenge&h_v=zen'

'''
Given a sequence of  integers,  where each element is distinct and satisfies . 
For each  where , that is  increments from  to , find any integer  such that  and keep a history of the values of  in a return array.
'''

def permutationEquation(p):
    n = len(p)
    x = list(range(1, n+1))
    print(x)
    
    y = [p.index(item) + 1 for item in x]
    result = [p.index(item) + 1 for item in y]
    
    return result
    
p = [5, 2, 1, 3, 4]

result = permutationEquation(p)
print('\n'.join(map(str, result)))