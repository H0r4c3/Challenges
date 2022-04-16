'https://py.checkio.org/en/mission/seven-segment/'

'''
You have a device that uses a Seven-segment display to display 2 digit numbers. However, some of the segments aren't working and can't be displayed.

You will be given information on the lit and broken segments. 
You won't know whether the broken segment is lit or not. 
You have to count and return the total number that the device may be displaying.

Input: Two arguments. The first one contains the lit segments as a set of letters representing segments. The second one contains the broken segments as a set of letters representing segments.

Output: The total number that the device may be displaying.
'''

# Best Solution: 
# https://py.checkio.org/mission/seven-segment/publications/KareeO/python-3/first/share/421bf00708f1d0d7fb46bc64541efdfa/
def seven_segment(lit_seg, broken_seg):

    digit = ['abcdef', 'bc', 'abged', 'abgcd', 'fgbc', 'afgcd', 'afgcde', 'abc', 'abcdefg', 'abcdfg']
    num = [set(s.upper()).union(set(t)) for s in digit for t in digit]
    return len([s for s in num if lit_seg.union(broken_seg) >= s>= lit_seg])



# Another Best Solution: 
# https://py.checkio.org/mission/seven-segment/publications/MrPod/python-3/analog-is-better/?ordering=most_voted&filtering=all
nums = {'ABCDEF', 'BC', 'ABGED', 'ABGCD', 'FGBC', 'AFGCD', 'AFGCDE', 'ABC', 'ABCDEFG', 'ABCDFG'}

def seven_segment(lit, broken):
    return sum(set(lit) <= set(i) | set(j.lower()) <= set(lit) | set(broken) for i in nums for j in nums)



if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')