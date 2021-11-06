'https://py.checkio.org/en/mission/end-zeros/'

'''
Try to find out how many zeros a given number has at the end.
'''

def end_zeros(num: int) -> int:
    
    if num == 0:
        return 1
    
    if num < 10:
        return 0
    
    for i in range(1, len(str(num))):
        if num % (10**i) == 0:
            continue
        else: 
            return i-1
    
    return i

# another solution
def end_zeros_new(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))
    
num = 1000
result = end_zeros_new(num)
print(result)