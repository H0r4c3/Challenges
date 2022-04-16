'https://py.checkio.org/en/mission/making-change/'

'''
When making purchases, Nicola would like to use the minimum number of coins possible. 
For example, Outer Leftopia has coins with denomination 1, 3, and 5 shillings. 
He wants to buy a souvenir that costs 13 shillings. He can do that using two 5 shilling coins and one 3 shilling coin.

Input: Two arguments. The first argument is an int: the price of the purchase. The second is a list of ints: the denominations of available coins.

Output: int. The minimum number of coins Nicola can use to make the purchase. If the price cannot be made with the available denominations, return None .
'''

# My Solution (has a bug!!!)
def checkio(price, denominations):
    """
        return the minimum number of coins that add up to the price
    """
    # def calc_remainder(price, denom):
    #     return price // denom
    
    result = 0
    
    for denom in denominations[: : -1]:
        print(f'denom = {denom}')
        
        if price < denom:
            continue
        
        rem = price % denom
        print(f'rem = {rem}')
        
        if rem > 0:
            result += price // denom
            print(f'result_intermed = {result}')
            price = rem
        elif rem == 0:
            print(f'result_rem_zero = {result + 1}')
            return result + 1
    
    print(f'result_final = {result}')        
    return result if (result !=0 and rem ==0) else None


# Best Solution:
# https://py.checkio.org/mission/making-change/publications/gyahun_dash/python-3/first/share/9f41582567c790448ad528d2b4d35367/
def checkio_(price, denoms):
    sums = set()
    for number in range(1, price + 1):
        sums = {s + d for s in sums for d in denoms} or set(denoms)
        if price in sums: return number


# Best Solution:
# https://py.checkio.org/mission/making-change/publications/Sim0000/python-3/first/share/1b400684e886a8cbc0de49f1ef75cd5b/

def checkio_(price, denominations):
    table = [0] + [price + 1] * price
    for coin in denominations:
        for i in range(coin, price + 1):
            table[i] = min(table[i], table[i - coin] + 1)
    return table[price] if table[price] <= price else None
    # dynamic programming



if __name__ == '__main__':
    print("Example:")
    #print(checkio(8, [1, 3, 5]))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio(8, [1, 3, 5]) == 2
    #assert checkio(12, [1, 4, 5]) == 3
    #assert checkio(1,[3,4,5]) == None
    #assert checkio(4,[3,5]) == None
    assert checkio(123456,[1,6,7,456,678]) == 187
    print('Done!!!')