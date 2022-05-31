'https://py.checkio.org/en/mission/oil-pie/'

'''
There are 6 drones. The first group consists of 2 drones. They had divided the pie into 6 parts and took 2/6 of the pie. 
The remainder of the pie is 2/3 of the entire pie. Next returns a single drone, it doesn’t know about the original size of the pie, 
so it divides the remaining pie into 6 slices and takes 1 part. This leaves 10/18=5/9. The last group is 3 drones, which heard about 
the original size of the pie from Sophia. They took half of the original pie, so the remaining is 5/9 - 3/6 = 1/18

You are given an ordered array with sizes of the groups in the order they arrived. If a group knows about the initial pie size, then the size is positive. 
If not, then size will be negative. The recent example will given as (2, -1, 3).
'''
from fractions import Fraction
from functools import reduce

def divide_pie_(groups):
    denom = sum(map(abs, groups))
    print(denom)
    
    fracts = [Fraction(num, denom) for num in groups]
    print(fracts)
    
    rest = [None] * len(groups)
    
    if groups[0] < 0:
        rest[0] = 1 + Fraction(groups[0], denom)
    else:
        rest[0] = 1 - Fraction(groups[0], denom)
    print(rest[0])
    
    if groups[1] < 0:
        rest[1] = rest[0] + Fraction(groups[1]*rest[0], denom)
    else:
        rest[1] = rest[0] - Fraction(groups[1], denom)
    print(rest[1])
    
    if groups[2] < 0:
        rest[2] = rest[1] + Fraction(groups[2]*rest[1], denom)
    else:
        rest[2] = rest[1] - Fraction(groups[2], denom)
    print(rest[2])
    
    
    return rest[2].numerator, rest[2].denominator



def divide_pie(groups):
    denom = sum(map(abs, groups))
    print(denom)
    
    g = len(groups)
    
    rest = [None] * (g + 1)
    rest[0] = 1
    
    for i in range(g):
        if groups[i] < 0:
            rest[i+1] = rest[i] + Fraction(groups[i]*rest[i], denom)
        else:
            rest[i+1] = rest[i] - Fraction(groups[i], denom)
        print(f'rest[i] = {rest[i]}')
    
    print((rest[g].numerator, rest[g].denominator))
    return rest[g].numerator, rest[g].denominator




# Best Solution
# https://py.checkio.org/mission/oil-pie/publications/gyahun_dash/python-3/reduce/share/999953e2efc44ee7043d5bc1a44c04bc/

from fractions import Fraction
from functools import reduce

def divide_pie_(groups):
    total = sum(abs(drones) for drones in groups)
    fracs = [Fraction(drones, total) for drones in groups]
    rest = reduce(lambda rem, frac: rem - max(frac, - rem * frac), [1] + fracs)

    return rest.numerator, rest.denominator




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
    print('Done!!!')