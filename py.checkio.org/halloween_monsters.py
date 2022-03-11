'https://py.checkio.org/en/mission/halloween-monsters/'

'''
You are given a string as an input value. You have to use it to make monster names and return the maximum number. You can call only 9 kinds of monsters:

frankenstein
ghost
jack
mummy
skeleton
vampire
werewolf
witch
zombie
NOTE:
You can make multiple monster names of the same kind.
You don't need to use all the characters.
If you can't make a monster name, return 0.
'''

MONSTERS = '''
skeleton
ghost
jack
vampire
witch
mummy
zombie
werewolf
frankenstein
'''

def rotate_list(my_list):
    list_of_lists = list()
    for _ in range(len(my_list)):
        my_list = my_list[1:] + my_list[:1]
        list_of_lists.append(my_list)
    
    return list_of_lists

result_monsters = list()
def monsters_in_spell(spell, list_of_monsters):    
    global result_monsters
    
    while list_of_monsters:
        monster = list_of_monsters[0]
        print(monster)
        print(spell)
        spell2 = spell
        matched_list = list()
        for c in monster:
            if c in spell2:
                matched_list.append(True)
                spell2 = spell2.replace(c, '', 1)
            else:
                matched_list.append(False)
        print(f'matched_list = {matched_list}')
        
        if all(matched_list):
            result_monsters.append(monster)
            print(f'result_monsters = {result_monsters}')
            
            for c in monster:
                spell = spell.replace(c, '', 1)
            print(f'Remaining spell = {spell}')
            
            if spell == None:
                return result_monsters
            
            monsters_in_spell(spell, list_of_monsters)
            
        else:
            del list_of_monsters[0]
            print(f'Remaining monsters = {list_of_monsters}')
            print(f'result_monsters = {result_monsters}')
            
    return result_monsters

# My Solution (has a bug!!!)
def halloween_monsters(spell: str)-> int:
    result_monsters = list()
    result_list = list()
    
    list_of_monsters = MONSTERS.splitlines()[1:]
    print(f'Starting list_of_monsters = {list_of_monsters}')
    print(f'Starting result_monsters = {result_monsters}')
    
    
    #result_monsters = monsters_in_spell(spell, list_of_monsters)
    #print(f'Final list = {result_monsters}')
    
    #return len(result_monsters)
    
    list_of_lists = rotate_list(list_of_monsters)
    
    for list_of_monsters in list_of_lists:
        result_monsters = monsters_in_spell(spell, list_of_monsters)
        print(f'Final list =  {result_monsters}')
        
        result_list.append(len(result_monsters))
        print(result_list)
 
    return max(result_list)



# Best Solution: 
# https://py.checkio.org/mission/halloween-monsters/publications/tom-tom/python-3/second/share/5b7ce897d02331ce5b054b0d7468c14f/

from collections import Counter

#MONSTERS = 'skeleton ghost jack vampire witch mummy zombie werewolf frankenstein'

def halloween_monsters_(spell: str)-> int:
    monsters = list(map(Counter, MONSTERS.split()))
    
    def result(pool):
        return max((result(pool - monster) + 1 for monster in monsters if all(pool[key] >= value for key, value in monster.items())), default=0)
                    
    return result(Counter(spell))


if __name__ == '__main__':
    assert halloween_monsters('casjokthg') == 2, 'jack ghost'
    assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
    assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
    assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
    assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'
    assert halloween_monsters("mhedarnmsxfjbpivdhwcdpfwsrkiuhpjoglferwzqridkbjvyqtnomaaeyinggftqvateloozhjbxcuxxgqllwsubkunsz") == 8, 'NOT skeleton, skeleton'
    print("Your spell seem to be okay. It's time to check.")