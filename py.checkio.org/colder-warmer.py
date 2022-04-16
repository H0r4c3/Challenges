'https://py.checkio.org/en/mission/colder-warmer/'

'''
Let's play a game of hide and seek. You have been given a map of 10x10 cells and in one of the cells we've hidden your goal. 
You can move to and from any cell in the field. On each move you'll get informed if the move places you closer or further away from your goal, 
compared to your previous location. Your function compiles data about previous steps, each step is a list of list, 
where first and second elements are your coordinates (row and column) and third is the info on how much closer you've 
gotten (colder or warmer) -- "colder" is -1, "warmer" is 1 and "same" is 0.
'''

# https://py.checkio.org/mission/colder-warmer/publications/_Chico_/python-3/first/share/1a6c9e620b32de1412e98f4c79764927/

def checkio(steps):
    if len(steps) == 12:
        x = sum([x[2]+1 for x in steps[2:7]])
        y = sum([x[2]+1 for x in steps[7:12]])
        return [x if x < 10 else 9, y if y < 10 else 9]
    r = "0020406080909294969899"
    return [int(r[2*len(steps)-2]), int(r[2*len(steps)-1])]


if __name__ == "__main__":
    # This part is using only for self-checking and not necessary for auto-testing
    from math import hypot

    MAX_STEP = 12

    def check_solution(func, goal, start):
        prev_steps = [start]
        for step in range(MAX_STEP):
            row, col = func([s[:] for s in prev_steps])
            if [row, col] == goal:
                return True
            if 10 <= row or 0 > row or 10 <= col or 0 > col:
                print("You gave wrong coordinates.")
                return False
            prev_distance = hypot(
                prev_steps[-1][0] - goal[0], prev_steps[-1][1] - goal[1]
            )
            distance = hypot(row - goal[0], col - goal[1])
            alteration = (
                0
                if prev_distance == distance
                else (1 if prev_distance > distance else -1)
            )
            prev_steps.append([row, col, alteration])
        print("Too many steps")
        return False

    assert check_solution(checkio, [7, 7], [5, 5, 0]), "1st example"
    assert check_solution(checkio, [5, 6], [0, 0, 0]), "2nd example"
    print('Done!')