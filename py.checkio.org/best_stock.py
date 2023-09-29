'https://py.checkio.org/en/mission/best-stock/'

'''
You are given the current stock prices. You have to find out which stocks cost more.

Input: The dictionary where the market identifier code is a key and the value is a stock price.

Output: The market identifier code (ticker symbol) as a string.
'''

def best_stock_(data: dict) -> str:
    return max(data, key = lambda val: data[val])


def best_stock_(data: dict) -> str:
    return sorted(data.items(), key = lambda x: x[1], reverse=True)[0][0]


# Best Solution: https://py.checkio.org/mission/best-stock/publications/kdim/python-3/first/

def best_stock(data: dict) -> str:
    return next(iter(sorted(data,key=data.get,reverse=True)))


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")