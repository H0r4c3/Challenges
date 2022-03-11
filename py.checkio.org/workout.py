'https://py.checkio.org/en/mission/workout/'

'''
Sam has prepared a fitness program so that he can become stronger! The program is made of N sessions. 
During the i-th session, Sam will do a certain amount of pushups. The number of pushups he does in each session is strictly increasing.

The difficulty of his fitness program is equal to the maximum difference in the number of pushups between any two consecutive training sessions.

To make his program less difficult, Sam has decided to add up to K additional training sessions to his fitness program. 
'''


from typing import List

# Solution nr. 1 (using itertools)
import itertools
def workout(sessions: List[int], additional: int) -> int:
    p = itertools.pairwise(sessions)
    
    diff = sorted([y-x for x,y in p])
    print(diff)
    
    for i in range(additional):
        split1 = diff[-1] // 2
        split2 = diff[-1] - split1
        diff.pop()
        diff.extend([split1, split2])
        diff = sorted(diff)
    print(diff)
    
    result = max(diff)
    print(result)
    return result


# Solution nr. 2 (using zip())
def workout_(sessions: List[int], additional: int) -> int:
    p = [y-x for x,y in zip(sessions, sessions[1:])]
    print(p)
    
    diff = sorted(p)
    print(diff)
    
    for i in range(additional):
        split1 = max(diff) // 2
        split2 = max(diff) - split1
        diff.remove(max(diff))
        diff.extend([split1, split2])
        diff = sorted(diff)

    print(diff)
    
    result = max(diff)
    print(result)
    return result


# Best Solution: 
# https://py.checkio.org/mission/workout/publications/fokusd/python-3/brute-force-without-binary-search/?ordering=most_voted&filtering=all

def workout(sessions: List[int], additional: int) -> int:
    max_diff = max(sessions[i] - sessions[i - 1] for i in range(1, len(sessions)))
    for diff in range(1, max_diff + 1):
        required = sum(((sessions[i] - sessions[i - 1]) - 1) // diff for i in range(1, len(sessions)))
        if required <= additional:
            return diff
        


if __name__ == '__main__':
    print("Example:")
    #print(workout([100, 200, 230], 1))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert workout([100, 200, 230], 1) == 50,     "First"
    assert workout([10, 13, 15, 16, 17], 2) == 2, "Second"
    assert workout([9, 10, 20, 26, 30], 6) == 3,  "Third"
    assert workout([18,44,48,92,120,150,191,224,254,282,331,381,395,405,414,428,435,454,483,488,518,568,572,606,639,658,674,704,740,756,798,800,842,858,874,916,941,946,992,1036,1078,1108,1120,1140,1146,1148,1154,1163,1201,1223,1246,1262,1292,1298,1344,1381,1400,1440,1444,1462,1482,1514,1553,1572,1613,1653,1666,1684,1733,1766,1792,1803,1842,1885,1892,1902,1944,1979,2028,2073,2086,2135,2144,2185,2228,2269,2281,2304,2312,2357,2381,2392,2424,2426,2475,2501,2527,2536,2560,2569,2577,2609,2648,2682,2721,2765,2800,2808,2823,2873,2904,2930,2935,2936,2983,3008,3034,3043,3050,3092,3101,3143,3150,3172,3188,3195,3211,3245,3286,3292,3294,3337,3386,3398,3426,3441,3481,3498,3499,3535,3549,3592,3627,3668,3679,3698,3727,3751], 424) == 8
    print("Coding complete? Click 'Check' to earn cool rewards!")