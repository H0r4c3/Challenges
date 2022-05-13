'https://py.checkio.org/en/mission/ground-for-the-house/'

'''
As the input data you will get the multiline string consists of '0' & '#'. where '0' means the empty piece of the ground and the '#' is the piece of your house. 
Your task is to count the minimal area of the rectangle ground which is enough for the building.
'''

def house(plan):
    plan_list = plan.split()
    cols = list()
    
    # in which strings from the list '#' exists
    rows = [i for i in range(len(plan_list)) if '#' in plan_list[i]]   
    print(f'rows = {rows}')
    
    # left and right positions of '#' for each string
    for item in plan_list:
        left = item.find('#')
        right = item.rfind('#')
        
        # only one '#' found
        if left == right:
            left = 0
        cols.append((left, right))         
    print(f'cols = {cols}')
    
    height = rows[-1] - rows[0] + 1 if rows else 0
    widths = [item[1] - item[0] + 1 for item in cols if item != (-1, -1)]
    print(widths)
    width = max(widths) if widths else 0
        
        
    print(height * width)
    return height * width
'''
00#0
0#00
#000
'''

# Best Solution:
# https://py.checkio.org/mission/ground-for-the-house/publications/Moff/python-3/first/?ordering=most_voted&filtering=all

def house_(plan):
    rows = set()
    cols = set()
    for i, row in enumerate(plan.splitlines()):
        for j, cell in enumerate(row):
            if cell == '#':
                rows.add(i)
                cols.add(j)
    return (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1) if rows else 0


if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12
    
    assert house('''
00#0
0#00
#000
''') == 9

    print("Coding complete? Click 'Check' to earn cool rewards!")