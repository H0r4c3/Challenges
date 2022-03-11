'https://py.checkio.org/en/mission/completely-empty/'

'''
You need to figure if a wellfounded and wellsized iterable is completely empty.

Some consequences of the above definitions:

any empty iterable is completely empty
a non-iterable is never completely empty
the only wellfounded string is '' , and it is completely empty
bytes, and (possibly nested) tuples/frozensets of them are always wellfounded and wellsized
{'': 'Nonempty'} is a wellfounded and completely empty iterable
after c=[];c.append(c) , c is a non-wellfounded iterable
itertools.repeat(()) is wellfounded but not wellsized
itertools.repeat(5) is wellfounded and wellsized
'''

def completely_empty(val):
    try:
        list_result = [completely_empty(item) for item in val]
        return all(list_result)
    except:
        return False



# Best Solution: https://py.checkio.org/en/mission/completely-empty/

def completely_empty_(val):
    return check(val, True)
    
def check(val, flag):
    try:
        for i in val:
            if flag:
                flag = check(i, flag)
        return flag
    except Exception as e:
        return False
    
    
    
# Another Best Solution:
# https://py.checkio.org/mission/completely-empty/publications/StefanPochmann/python-3/duh/?ordering=most_voted&filtering=all

def completely_empty_(val):
    try:
        return all(map(completely_empty, val))
    except:
        return False
    
	


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[],[1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[],[{'':'No WAY'}]]) == True
    assert completely_empty(type('', (), {'__getitem__': ().__getitem__})()) == True
    print('Done!')