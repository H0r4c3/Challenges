'https://py.checkio.org/en/mission/the-tower/'

'''
Your task is to return the maximum possible height of the tower built from the cubes in such a way that each of four its side sides are 
of the same color (4 sides - 4 colors, each side has its own color).
Each cube is described by a string of 6 letters in capital Latin characters which represent the color of the respective side 
(A — Azure, B — Blue, C — Cyan, G — Green, O — Orange, R — Red, S — Scarlet, V — Violet, W — White, Y — Yellow).

The sides are numbered in the following order: front, right, left, back, top, bottom. A cube doesn’t have two sides of the same color.
You may rotate each cube as you wish to build the tower.
'''

def tower(cubes):
    #replace this for solution
    return 0




# Best Solution: 
# https://py.checkio.org/mission/the-tower/publications/_Chico_/python-3/first/share/bed7e63057ecf424c2404e74af7dfd10/

def tower(cubes):
    
    from collections import Counter
    
    rot=[(0,1,3,2),(1,3,2,0),(3,2,0,1),(2,0,1,3),(0,4,3,5),(4,3,5,0),(3,5,0,4),
    (5,0,4,3),(4,1,5,2),(1,5,2,4),(5,2,4,1),(2,4,1,5)]
    L=[]
    for cub in cubes:
        L+=[tuple(cub[i] for i in pos) for pos in rot]
        L+=[tuple(cub[i] for i in pos[-1::-1]) for pos in rot]
    return max(Counter(L).values())


if __name__ == '__main__':
    print("Example:")
    print(tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']) == 3
    assert tower(['ABCGYW', 'CAYRGO', 'OCYWBA', 'ACYVBR', 'GYVABW']) == 1
    assert tower(['GYCABW', 'GYCABW', 'GYCABW', 'GYCABW', 'GYCABW']) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")