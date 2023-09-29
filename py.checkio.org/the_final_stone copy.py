'https://py.checkio.org/en/mission/the-final-stone/'

'''
You have a list of stones with different weights. The result of hitting two stones will be a new stone with a weight difference between the two stones.
Your goal is to find the weight of the final stone. If no stones left, the result is 0.

The algorithm is very simple:

get the two biggest stones in the batch
hit and get the resulting stone
put the resulting stone back in the batch.
'''    
import sys

def final_stone(stones: list[int]) -> int:
    print(f'stones = {stones}')
    len_list = len(stones)
        
    sys.setrecursionlimit(2000)
    
    def final_stone_recursion(stones):
        repetitions = 1
        
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        stones = sorted(stones)
        
        new_item = stones[-1] - stones[-2]
        stones = stones[:-2] + [new_item]
        repetitions += 1
        print(f'repetitions = {repetitions}')
        result = final_stone_recursion(stones)
        
        return result
    
    result = final_stone_recursion(stones)
    
    print(f'len_list = {len_list}')
    print(f'result = {result}')
    
    return result
   

# Best Solution: https://py.checkio.org/mission/the-final-stone/publications/review/clear/

from functools import reduce

def final_stone_(stones: list[int]) -> int:
    result = reduce(lambda a, b: abs(a-b), sorted(stones, reverse=True), 0)
    print(f'result = {result}')
    return result


#assert final_stone([list(range(1000000))]) == 0

print('Example:')

assert final_stone([3, 5, 1, 1, 9]) == 1
assert final_stone([1, 2, 3]) == 0
assert final_stone([1, 2, 3, 4]) == 0
assert final_stone([1, 2, 3, 4, 5]) == 1
assert final_stone([1, 1, 1, 1]) == 0
assert final_stone([1, 1, 1]) == 1
assert final_stone([1, 10, 1]) == 8
assert final_stone([1, 10, 1, 8]) == 0
assert final_stone([]) == 0
assert final_stone([1]) == 1
assert final_stone([10, 20, 30, 50, 100, 10, 20, 10]) == 10

big_list = [x for x in range(1000)]
assert final_stone(big_list) == 0
              
print("The mission is done! Click 'Check Solution' to earn rewards!")