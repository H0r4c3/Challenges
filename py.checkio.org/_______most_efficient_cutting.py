'https://py.checkio.org/en/mission/most-efficient-cutting/'

'''
Metal strips, pipes, rods, etc. are being delivered in lengths of 6000 millimeters (6 meters). We want to cut them into pieces of different lengths.

Write a piece of code that finds how to do this in the most efficient way, that is, with the least possible quantity of material wasted. 
You are given the requested pipe lengths (as a list of integers). 
You should find the most efficient way of cutting, and return the sum of the wasted pipe length.
'''

def most_efficient_cutting(bom):

    return 0
    
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert(most_efficient_cutting([3000, 2200, 2000, 1800, 1600, 1300]) == 100)
    assert (most_efficient_cutting([4000, 4000, 4000]) == 6000), "wasted: 3x2000"
    assert(most_efficient_cutting([1]) == 5999), "5999"
    assert(most_efficient_cutting([3001, 3001]) == 5998), "2x2999"
    assert(most_efficient_cutting([3000, 2200, 1900, 1800, 1600, 1300]) == 200), "2x5900"
    assert(most_efficient_cutting([3000]) == 3000)
    assert(most_efficient_cutting([3000, 2200, 2000, 1800, 1600, 1400]) == 0)
    
    print('"Run" is good. How is "Check"?')