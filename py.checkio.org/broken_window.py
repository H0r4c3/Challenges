'https://py.checkio.org/en/mission/broken-window/'

'''
You have to restore the broken window glass.

Input: The pieces of the broken window (list of lists of integers).

Output: The list of top pieces and list of bottom pieces (both are lists of integers).

The answer should be returned in the two lists (the upper list and lower list in that order).

In the output each piece is represented in the order given as input (starting with 0).
The bases of the pieces in the same list must always be adjacent to each other.
(In other words, one piece doesn't form both the upper and lower side of the window.)
It is not necessary to consider turning over piece.
'''



# Best Solution: 
# https://py.checkio.org/mission/broken-window/publications/przemyslaw.daniel/python-3/22-liner-fast-clean/?ordering=most_voted&filtering=all

def sliced(piece):
    return sum(([x, y] for x, y in zip(piece, piece[1:])), [])

def is_incorrect(up, down):
    return len({x+y for x, y in zip(up, down)}) > 1

def broken_window(pieces):
    stack = [([], [], [], [], list(enumerate(pieces)))]
    while stack:
        up, down, up_idx, down_idx, pieces = stack.pop()
        if is_incorrect(up, down):
            continue
        if not pieces and len(up) == len(down):
            return up_idx, down_idx
        for k in range(len(pieces)):
            (index, piece), _pieces = pieces[k], pieces[:k]+pieces[k+1:]
            if len(up) < len(down):
                piece = sliced(piece[::-1])
                stack += [(up+piece, down, up_idx+[index], down_idx, _pieces)]
            else:
                piece = sliced(piece)
                stack += [(up, down+piece, up_idx, down_idx+[index], _pieces)]
                


if __name__ == '__main__':

    def checker(func, pieces):
        answer = func(pieces)

        if not (isinstance(answer, (tuple, list))
                and len(answer) == 2
                and isinstance(answer[0], list) and isinstance(answer[1], list)):
            print('wrong type:', answer)
            return False

        if set(answer[0]+answer[1]) != set(range(len(pieces))):
            print('wrong value:', answer)
            return False

        tops = [list(reversed(pieces[t])) for t in answer[0]]
        bottoms = [pieces[b] for b in answer[1]]
        height = set()

        top = tops.pop(0)
        bottom = bottoms.pop(0)
        while True:
            height |= set(map(sum, zip(top, bottom)))
            if len(top) < len(bottom) and tops:
                bottom = bottom[len(top)-1:]
                top = tops.pop(0)
            elif len(top) > len(bottom) and bottoms:
                top = top[len(bottom)-1:]
                bottom = bottoms.pop(0)
            elif len(top) == len(bottom):
                if tops and bottoms:
                    top = tops.pop(0)
                    bottom = bottoms.pop(0)
                elif not tops and not bottoms:
                    break
                else:
                    return False
            else:
                return False

        return len(height) == 1

    print("Example:")
    print(broken_window([[0, 1], [0, 1]]))

    assert checker(broken_window, [[0, 3, 4, 1], [4, 0], [3, 0], [0, 1, 4, 0]])
    assert checker(broken_window, [[0, 1], [0, 1]])
    print("Coding complete? Click 'Check' to earn cool rewards!")