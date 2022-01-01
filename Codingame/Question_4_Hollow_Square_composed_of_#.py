
def hollow_square(n):
    
    print(n*'#')
    
    for i in range(n-2):
        print('#' + (n-2)*' ' + '#')
    
    print(n*'#')


n = 5
hollow_square(n)
