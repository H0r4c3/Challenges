'https://py.checkio.org/en/mission/knapsack-problem-2/share/9883dbd1752cd52cd44b2685a45c31ac/'

'''
This mission is dedicated to a famous and classical Knapsack Problem.

You are given a list of kinds of items that you want to put into knapsack. 
Item of each kind is a tuple of its value, weight and maximum amount (optional). 

You need to find a subset of items, such that:

- the total value of the items in subset is as large as possible;
- the total weight of items in subset is at most weight, that is capacity of the knapsack;
- for each kind of items you can select at most given amount items. If its not given - there is no restriction for amount.
'''

# https://www.educative.io/blog/0-1-knapsack-problem-dynamic-solution

# Knapsack brute-force recursion 
# The most obvious solution to this problem is brute force recursive. 
# This solution is brute-force because it evaluates the total weight and value of all possible subsets, 
# then selects the subset with the highest value that is still under the weight limit.

'''
Here’s a pseudo code explanation of how this program functions.

for each item 'i' starting from the end
  create a new set which INCLUDES item 'i' if the total weight does not exceed the capacity, and recursively process the remaining capacity and items
  create a new set WITHOUT item 'i', and recursively process the remaining items 
 
return the set from the above two sets with higher profit
'''


def knapsack_recursive(profits, weights, capacity, currentIndex):
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)

    return max(profit1, profit2)

#def knapsack(weight: int, items: list[tuple[int, int] | tuple[int, int, int]]) -> int:
def knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)

def main():
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  
main()


print("Example:")
#print(knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]))

# These "asserts" are used for self-checking
assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
assert knapsack(8, [(10, 10, 3)]) == 0
assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12
assert knapsack(15, [(7, 4, 1), (8, 5, 1), (6, 3, 1), (9, 6, 1)]) == 24
assert knapsack(20, [(10, 5, 1), (15, 8, 1), (7, 4, 1), (12, 6, 1), (4, 2, 1)]) == 38
assert knapsack(40, [(10, 5, 3), (15, 8, 2), (7, 4, 1), (12, 6, 2), (4, 2, 4)]) == 78
assert knapsack(50, [(20, 10, 1), (15, 8, 2), (18, 12), (10, 5, 1), (8, 4), (5, 3, 4)]) == 100

print("The mission is done! Click 'Check Solution' to earn rewards!")