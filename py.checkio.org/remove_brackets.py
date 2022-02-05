'https://py.checkio.org/en/mission/remove-brackets/'

'''
Your task is to restore the balance of open and closed brackets by removing the unnecessary ones, while trying to use the minimum number of deletions.

Only 3 types of brackets (), [] and {} can be used in the given string.
'''
# from collections import Counter
# def remove_brackets(line: str) -> str:
#     count = Counter(line)
#     d = dict(count.most_common())
#     print(d)
    
#     def replacings(line, d, s1, s2):
#         # if d.get(s1) == None:
#         #     return line
#         # elif d.get(s2) == None:
#         #     return line
        
#         # if s1 or s2 not found, replace the value with 0
#         repl = d.get(s1, 0) - d.get(s2, 0)
#         print(f'repl = {repl}')
        
#         if repl > 0:
#             # replace from the end of the string
#             #line = line[::-1].replace(s1, '', repl)[::-1]
            
#             line = line.replace(s1, '', repl)
#         elif repl < 0:
#             #line = line[::-1].replace(s2, '', abs(repl))[::-1]
            
#             line = line.replace(s2, '', abs(repl))
            
#         return line
    
           
#     result = replacings(line, d, '(', ')')
#     #result = replacings(line, d, '[', ']')
#     #result = replacings(line, d, '{', '}')
            
              
#     print(result)
#     return result
        
            
from itertools import combinations            
def remove_brackets(line: str) -> str:
    
    def replacings(line: str) -> bool:
        while True:
            if '()' in line or '[]' in line or '{}' in line:
                line = line.replace('()','').replace('[]','').replace('{}','')
            else: return not line
        
   
    for i in range(len(line)+1):
        for comb in combinations(range(len(line)), i):
            result = ''.join(k for c, k in enumerate(line) if c not in comb)
            #print(result)
            
            if replacings(result): return result




if __name__ == "__main__":
    print("Example:")
    #print(remove_brackets("(()()"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets("(()()") == "()()"
    assert remove_brackets("[][[[") == "[]"
    assert remove_brackets("[[(}]]") == "[[]]"
    assert remove_brackets("[[{}()]]") == "[[{}()]]"
    assert remove_brackets("[[[[[[") == ""
    assert remove_brackets("[[[[}") == ""
    assert remove_brackets("") == ""
    assert remove_brackets("[(])") == "()"
    print("Coding complete? Click 'Check' to earn cool rewards!")