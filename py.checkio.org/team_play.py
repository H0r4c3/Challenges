'https://py.checkio.org/en/mission/team-play-2/'

'''
Input: Three arguments. Two lists of integers of equal size representing team's stats. 
An integer - a number of team's members that have to be occupied with cutting.

Output: An integer - the maximum score which can be obtained by the team.
'''

# My Solution = Brute Force (Error = ErrorProcessOutOfSystemLimits)

from itertools import combinations
from typing import List

def cuts_and_bends(my_tuple, bend):
    idx_cut = list()
    total_tuple = list()
    
    for item in my_tuple:
        idx_cut.append(item[0])
        total_tuple.append(item[1])
    print(idx_cut)
    print(total_tuple)
    idx_bend = [idx for idx in idx_all if idx not in idx_cut]
    print(idx_bend)
    for idx in idx_bend:
        total_tuple.append(bend[idx])
    print(total_tuple)
    
    return total_tuple
        
    

def max_score_(cut: List[int], bend: List[int], k: int) -> int:
    global idx_all
    idx_all = range(len(cut))
    enum_cut = list(enumerate(cut))
    sums = list()
    
    all_possible_cuts = list(combinations(enum_cut, k))
    print(all_possible_cuts)
    for item in all_possible_cuts:
        total_tuple = cuts_and_bends(item, bend)
        sums.append(sum(total_tuple))
    
    print(sums)
    
    print(max(sums))    
    return max(sums)


# Best Solution:
# https://py.checkio.org/mission/team-play-2/publications/kurosawa4434/python-3/zip/share/1b4f4bccaa59faabd86618a3fb08a5fb/

from typing import List

def max_score(cut: List[int], bend: List[int], k: int) -> int:
    print(sum(bend + sorted(c - b for c, b in zip(cut, bend))[-k:]))
    return sum(bend + sorted(c - b for c, b in zip(cut, bend))[-k:])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    #print(max_score([4, 2, 1], [2, 5, 3], 2))

    assert max_score([4, 2, 1], [2, 5, 3], 2) == 10, "Your team can do better."
    assert max_score([7, 1, 4, 4], [5, 3, 4, 3], 2) == 18, "Bet you can improve this."
    assert max_score([5, 5, 5], [5, 5, 5], 1) == 15, "Almost there!"
    assert max_score([13,9,89,17,63,58,67,67,100,43,20,87,8,89,6,10,42,75,26,12,34,97,
                      95,7,21,49,57,24,77,54,32,72,79,100,59,72,31,39,61,29,99,46,43,
                      90,21,21],[12,28,10,4,81,6,71,59,33,56,10,10,83,10,68,29,81,39,63,
                      99,22,4,36,60,57,94,58,61,65,58,62,79,92,15,75,65,36,84,5,16,57,52,75,29,24,15],25) == 3004
    print("Coding complete? Click 'Check' to earn cool rewards!")