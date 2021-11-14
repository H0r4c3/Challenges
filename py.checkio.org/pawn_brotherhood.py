'https://py.checkio.org/en/mission/pawn-brotherhood/'

'''
You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.
'''

def safe_pawns(pawns: set) -> int:
    counter = 0
    for item in pawns:
        #print(str(chr((ord(item[0]) - 1))))
        #print(str(int(item[1]) - 1))
        guardian1 = str(chr((ord(item[0]) - 1))) + str(int(item[1]) - 1)
        guardian2 = str(chr((ord(item[0]) + 1))) + str(int(item[1]) - 1)
        if (guardian1 in pawns) or (guardian2 in pawns):
            counter += 1
        else:
            continue
   
    return counter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1