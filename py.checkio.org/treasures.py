'https://py.checkio.org/en/mission/treasures/'

'''
As input you'll receive the information about the vault contents in the following format: {'golden coin': {'price': 100, 'weight': 50, 'amount': 200}, 
'silver coin': {'price': 10, 'weight': 20, 'amount': 1000} , 'ruby': {'price': 1000, 'weight': 200, 'amount': 2}}, where 
price is measured in the standard units of your country's currency, weight is measured in grams, and amount is measured in pieces.
In addition, you'll also have a weight limit (in kilograms), over which you won't be able to carry.

Your task is to collect such a set of treasures so that their total weight doesn't exceed the limit, and their total cost was as high as possible.
'''

def treasures(info, limit):
    limit = limit * 1000
    
    # prices, weights, amounts
    r_p, r_w, r_a = info.get('ruby').values()
    g_p, g_w, g_a = info.get('golden coin').values()
    s_p, s_w, s_a = info.get('silver coin').values()
    
    # calculate the price per gram
    r_gram = r_p / r_w
    g_gram = g_p / g_w
    s_gram = s_p / s_w
    print(r_gram, g_gram, s_gram)
    
    if g_gram > r_gram:
        
        g = round(limit // g_w)
        if g > 0:
            if g >= g_a:
                limit = limit - g_a * g_w
                g = g_a
            else:
                limit = limit - g * g_w
        else:
            return []
        
        
        r = round(limit // r_w)
        if r > 0:
            if r >= r_a:
                limit = limit - r_a * r_w
                r = r_a
            else:
                limit = limit - r * r_w    
        else:
            return [f'golden coin: {g}']
        
        
        s = round(limit // s_w)
        if s > 0:
            if s >= s_a:
                limit = limit - s_a * s_w
                s = s_a
            else:
                limit = limit - s * s_w
        else:
            print([f'golden coin: {g}', f'ruby: {r}'])
            return [f'golden coin: {g}', f'ruby: {r}']
        
        print([f'golden coin: {g}', f'silver coin: {s}', f'ruby: {r}'])
        return [f'golden coin: {g}', f'silver coin: {s}', f'ruby: {r}']
    
    else:
        
        r = round(limit // r_w)
        if r > 0:
            if r >= r_a:
                limit = limit - r_a * r_w
                r = r_a
            else:
                limit = limit - r * r_w    
        else:
            return []
            
        g = round(limit // g_w)
        if g > 0:
            if g >= g_a:
                limit = limit - g_a * g_w
                g = g_a
            else:
                limit = limit - g * g_w
        else:
            return [f'ruby: {r}']
            
        s = round(limit // s_w)
        if s > 0:
            if s >= s_a:
                limit = limit - s_a * s_w
                s = s_a
            else:
                limit = limit - s * s_w
        else:
            return [f'golden coin: {g}', f'ruby: {r}']
        
        print([f'golden coin: {g}', f'silver coin: {s}', f'ruby: {r}'])
        return [f'golden coin: {g}', f'silver coin: {s}', f'ruby: {r}']


# Best Solution:
# https://py.checkio.org/mission/treasures/publications/Moff/python-3/first/share/b9a9c4e1d6d65f9778947089b596bd3d/

from collections import defaultdict
import math

def treasures_(safe, limit):
    limit = math.floor(limit * 1000)
    items = []
    for k, v in safe.items():
        items.extend([(k, v['weight'], v['price']) for _ in range(min(v['amount'], limit // v['weight']))])
    table = [[0] * (limit + 1) for _ in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, wt, val = items[j - 1]
        for w in range(1, limit + 1):
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w], table[j - 1][w - wt] + val)

    d = defaultdict(int)
    for j in range(len(items), 0, -1):
        if table[j][limit] != table[j - 1][limit]:
            item, wt, val = items[j - 1]
            d[items[j - 1][0]] += 1
            limit -= wt
    return [f'{k}: {d[k]}' for k in ('golden coin', 'silver coin', 'ruby') if d[k]]



# Best Solution:
# https://py.checkio.org/mission/treasures/publications/przemyslaw.daniel/python-3/11-liner-get-rich/?ordering=most_voted&filtering=all

def treasures(info, limit):
    price_per_gram = sorted(info, key=lambda x: info[x]['price'] / info[x]['weight'])

    result, weight = {}, int(1000*limit)
    for valuable in reversed(price_per_gram):
        amount = min(weight // info[valuable]['weight'], info[valuable]['amount'])
        result[valuable] = amount
        weight -= amount*info[valuable]['weight']

    valuables = 'golden coin,silver coin,ruby'.split(',')
    return [f"{valuable}: {result[valuable]}" for valuable in valuables if result[valuable]]


if __name__ == '__main__':
    print("Example:")
    print(treasures({'golden coin': 
                        {'price': 100, 'weight': 50, 'amount': 200}, 
                     'silver coin': 
                        {'price': 10, 'weight': 20, 'amount': 1000}, 
                     'ruby': 
                        {'price': 1000, 'weight': 200, 'amount': 2}}, 5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert treasures({'golden coin': 
                         {'price': 100, 'weight': 50, 'amount': 200}, 
                      'silver coin': 
                         {'price': 10, 'weight': 20, 'amount': 1000}, 
                      'ruby': 
                         {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
                          'golden coin: 92', 'ruby: 2']
    assert treasures({'golden coin': 
                         {'price': 100, 'weight': 50, 'amount': 100}, 
                      'silver coin': 
                         {'price': 10, 'weight': 20, 'amount': 100}, 
                      'ruby': 
                         {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5) == [
                          'golden coin: 100', 'silver coin: 100', 'ruby: 1']
                         
    assert treasures({"golden coin":
                        {"price":100,"weight":10,"amount":100},
                    "silver coin":
                        {"price":10,"weight":10,"amount":100},
                    "ruby":
                        {"price":1000,"weight":200,"amount":5}}, 1.8) == ["golden coin: 100", "ruby: 4"]
    
    assert treasures({"golden coin":
                        {"price":250,"weight":10,"amount":30},
                    "silver coin":
                        {"price":30,"weight":5,"amount":200},
                    "ruby":
                        {"price":10000,"weight":250,"amount":7}}, 2.75) == ["golden coin: 30", "silver coin: 140", "ruby: 7"]
    
    print("Coding complete? Click 'Check' to earn cool rewards!")