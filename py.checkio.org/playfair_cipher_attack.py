'https://py.checkio.org/en/mission/playfair-cipher-attack/share/3d4b62b955c8fedf5f7a004001047145/'

'''
Playfair cipher used a 5x5 key table filled with 25 letters of English alphabet in random order (letter J is omitted). 
Message is broken up into pairs of letters (each pair must consist of two different letters, 
otherwise letter X is inserted between them). Then each bigram is encrypted according to following rules:

1. If both letters are in the same row of key table, each is replaced by the letter to it's immediate right (the last column wraps around to the first);

2. If the letters appear in the same column - each is replaced with the one below it (the bottom row wraps around to the top);

3. If the letters are at diagonally opposite corners of a rectangle, they are replaced with letters at other two corners. 
The order is important - the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair
'''

# Best Solution: 
# https://py.checkio.org/mission/playfair-cipher-attack/publications/Vykers/python-3/recursive-search/?ordering=most_voted&filtering=all


from itertools import product

def encrypt(message, key_table):               #encrypts message using playfair key (from Playfair mission)
    back_key = {key_table[i]: i for i in key_table}
    answer = ''
    for i in range(0, 15, 2):
        a, b = message[i], message[i + 1]
        ax, ay = key_table[a]
        bx, by = key_table[b]
        if  bx == ax:
            cx, cy = ax, (ay + 1) % 5
            dx, dy = bx, (by + 1) % 5
        elif ay == by:
            cx, cy = (ax + 1) % 5, ay
            dx, dy = (bx + 1) % 5, by    
        else:
            cx, cy = ax, by
            dx, dy = bx, ay
        answer += back_key[(cx, cy)] + back_key[(dx, dy)]
    return answer


def resolve(table, pair):            #given a pair of bigrams, finds and checks coordinates for second bigram
    a, b, c, d = pair
    update_ = {a: table[a], b: table[b]}
    
    for (i, j, k) in [(c, a, b), (d, b, a)]:
        if table[j][1] == table[k][1]:
            coords = ((table[j][0] + 1) % 5, table[j][1])
        elif table[j][0] == table[k][0]:
            coords = (table[j][0], (table[j][1] + 1) % 5)
        else:
            coords = (table[j][0], table[k][1])
            
        if i in table:
            if table[i] != coords:
                raise AssertionError
        elif coords in table.values():
            raise AssertionError
        else:
            update_[i] = coords

    return update_
              

def make_variants(pair, table):                        #makes variants where letters of a pair might be in table
    free_cells = {i for i in product(range(5), range(5)) if i not in table.values()}
    a, b, c, d = pair 
    variants = [] 
    a_coord = free_cells if a not in table else {table[a]}
    for a_ in a_coord:
        b_coord = free_cells - {a_} if b not in table else {table[b]}
        for b_ in b_coord:
            try:
                new_table = table.copy()
                new_table.update({a: a_, b: b_})
                v = resolve(new_table, a + b + c + d)
                variants.append(v)
            except: 
                continue
                
    return variants


def search_step(candidate_table, unused_pairs):            #recursive search step
    if not unused_pairs:
        return candidate_table
    
    next_pair = max(unused_pairs, key=lambda x: sum([l in candidate_table for l in x])) #important!
    variants = make_variants(next_pair, candidate_table)
    for v in variants:
        new_table = candidate_table.copy()
        new_table.update(v)
        result = search_step(new_table, unused_pairs - {next_pair})
        if result is not None:
            return result


def playfair_attack(plain, crypto):
    pairs = [(plain[i:i+2] + crypto[i:i+2]) for i in range(0, len(plain), 2)]
    start = pairs[0]          
    key_table = search_step({start[0]: (0,0)}, set(pairs))
    unknown = list(set('abcdefghiklmnopqrstuvwxyz') - set(key_table.keys()))
    if len(unknown) == 1:
        for xy in product(range(5), range(5)):
            if xy not in key_table.values():
                key_table[unknown[0]] = xy
                break

    return encrypt('topsecretmessage', key_table)


if __name__ == "__main__":
    print("Example:")
    # print(
    #     playfair_attack(
    #         "sixcrazykingsvowedtoabolishmyquitepitifulioust",
    #         "zlgrcekqztvoolunhbvkemsvlzadnpzflrqlvlhwtluzkl",
    #     )
    # )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        playfair_attack(
            "sixcrazykingsvowedtoabolishmyquitepitifulioust",
            "zlgrcekqztvoolunhbvkemsvlzadnpzflrqlvlhwtluzkl",
        )
        == "vklprhcrixbpzebc"
    )

    assert (
        playfair_attack(
            "pythonsxstandardlibraryisveryextensiveofferingawiderangeofstuffx",
            "aiwblarskwphydowzehmhoieksxlixgwvufxlvzqvizxbehdycxlphyxzqkwcvsi",
        )
        == "dmhfiulxgbxvqhyx"
    )

    assert (
        playfair_attack(
            "zombiesquicklyatetwelveofmyneighboursx",
            "uzuywyksmzdcvhfgtnftonbnkfevywlgxzmxzd",
        )
        == "xnzpchtyrfcwpkth"
    )
    
    assert (playfair_attack("discoelysiumanisometricdetectiverpgwhatkindofcopareyou",
                            "yuiqrfxluspueqsuuhabospyablnxsebunfdtfhqrcwulkukeslvir"
            )
        == 'hsqulnnbmbarqtef')

    print("Coding complete? Click 'Check' to earn cool rewards!")