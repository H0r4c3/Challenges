'https://py.checkio.org/en/mission/texas-referee/'

'''
Input: A list of cards as a string.

Output: The best hand as a string.
'''

RANKS = "23456789TJQKA"
SUITS = "scdh"


def texas_referee(cards_str):
    return ""


# Best Solution:
# https://py.checkio.org/mission/texas-referee/publications/yoichi/python-3/first/share/f6c86b504bdccde584106a6b88e6f4f5/

RANKS = "AKQJT98765432"
SUITS = "hdcs"
KEY = lambda c: RANKS.find(c[0])*len(SUITS) + SUITS.find(c[1])


def get_straight_flush(cards):
    for c in sorted(cards, key=KEY):
        ci = RANKS.find(c[0])
        if ci + 5 > len(RANKS):
            return None
        for i in range(1, 5):
            if (RANKS[ci + i] + c[1]) not in cards:
                break
        else:
            return [RANKS[ci + i] + c[1] for i in range(5)]
    else:
        return None


def get_same_kinds(a, cards):
    results = []
    for n in a:
        for r in sorted(set(c[0] for c in cards), key=lambda c: RANKS.find(c)):
            same_kind = list(filter(lambda c: c[0] == r, cards))
            if len(same_kind) == n:
                results += same_kind
                cards = list(filter(lambda c: c not in same_kind, cards))
                break
        else:
            return None
    return results + sorted(cards, key=KEY)[:5-len(results)]


def get_flush(cards):
    for s in SUITS:
        same_suit = list(filter(lambda c: c[1] == s, cards))
        if len(same_suit) == 5:
            return same_suit
    return None


def get_straight(cards):
    cards = sorted(cards, key=KEY)
    ranks = "".join(map(lambda c: c[0], cards))
    for i in range(len(RANKS)-5):
        results = []
        ri = 0
        for r in RANKS[i:i+5]:
            ri = ranks.find(r, ri)
            if ri < 0:
                break
            results.append(cards[ri])
        else:
            return results
    return None


def get_high_card(cards):
    return sorted(cards, key=KEY)[:5]


PREDICATES = [get_straight_flush,
              [4],  # four of a kind
              [3, 2],  # full house
              get_flush,
              get_straight,
              [3],  # three of a kind
              [2, 2],  # two pair
              [2],  # one pair
              get_high_card]


def texas_referee(cards_str):
    cards = cards_str.split(",")
    for pred in PREDICATES:
        if isinstance(pred, list):
            results = get_same_kinds(pred, cards)
        else:
            results = pred(cards)
        if results:
            break
    return ",".join(sorted(results, key=KEY)[:5])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th", "High Straight Flush"
    assert texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d", "Straight Flush"
    assert texas_referee("5c,7h,7d,9s,9c,8h,6d") == "9c,8h,7h,6d,5c", "Straight"
    assert texas_referee("Ts,2h,2d,3s,Td,3c,Th") == "Th,Td,Ts,3c,3s", "Full House"
    assert texas_referee("Jh,Js,9h,Jd,Th,8h,Td") == "Jh,Jd,Js,Th,Td", "Full House vs Flush"
    assert texas_referee("Js,Td,8d,9s,7d,2d,4d") == "Td,8d,7d,4d,2d", "Flush"
    assert texas_referee("Ts,2h,Tc,3s,Td,3c,Th") == "Th,Td,Tc,Ts,3c", "Four of Kind"
    assert texas_referee("Ks,9h,Th,Jh,Kd,Kh,8s") == "Kh,Kd,Ks,Jh,Th", "Three of Kind"
    assert texas_referee("2c,3s,4s,5s,7s,2d,7h") == "7h,7s,5s,2d,2c", "Two Pairs"
    assert texas_referee("2s,3s,4s,5s,2d,7h,8h") == "8h,7h,5s,2d,2s", "One Pair"
    assert texas_referee("3h,4h,Th,6s,Ad,Jc,2h") == "Ad,Jc,Th,6s,4h", "High Cards"
    print('Done!!!')