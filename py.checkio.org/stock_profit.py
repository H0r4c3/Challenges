'https://py.checkio.org/en/mission/stock-profit/share/2f5c97a5ef8a452dbff6e23a449eab7b/'

'''
You are a broker with a single chance to buy stock and sell stock. Having an array of prices, pick the best time to buy stock and sell stock to maximize the profit.

“short-selling” (sell first, buy later) is not allowed in this market.

Your profit is zero when it is impossible to get profit at all. The size of pricing can't be less than 2.

Input: Array of int. Stock prices.

Output: Int. Maximum possible profit.
'''
from itertools import combinations

def stock_profit(stock: list) -> int:
    all_comb = list(combinations(stock, 2))
    profit_list = [item[1] - item[0] for item in all_comb if item[1] > item[0]]
    
    return max(profit_list) if profit_list != [] else 0


print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))

assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0

print("You are the best broker here! Click 'Check' to earn cool rewards!")