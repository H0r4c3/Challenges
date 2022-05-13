'https://py.checkio.org/en/mission/the-ship-teams/'

'''
You have to divide all your crew members into 2 teams with the next rules: those who are elder than 40 y.o. or 
younger than 20, should be on the first ship and all the others - on the second. 
It will helps the young sailors gain the experience of the elder colleagues. The input data will be the dictionary where keys will be the surnames of the sailors and the values will be their ages. 
After the crew formating, you should sort all of the sailors in the alphabetical order in the each list of surnames.
'''

def two_teams(sailors):
    
    list1 = sorted([key for key, value in sailors.items() if (value<20 or value>40)])
    list2 = sorted([key for key, value in sailors.items() if 20<=value<=40])
    print(list1)
    print(list2)
    
    return [
        list1,
        list2
    ]

if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34, 
        'Wesson': 22, 
        'Coleman': 45, 
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'], 
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'], 
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")