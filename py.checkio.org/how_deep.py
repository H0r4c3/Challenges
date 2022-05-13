'https://py.checkio.org/en/mission/how-deep/'

'''
You are given a tuple that consists of integers and other tuples, which in turn can also contain tuples.

Your task is to find out how deep this structure is or how deep the nesting of these tuples is.
'''

# My first Solution
def how_deep_(structure):
    try:
        return 1 + max(map(how_deep, structure)) if structure != () else 1
    except:
        return 0
    

# My second Solution (NOK)
import re
def how_deep_(structure):
    struct = str(structure)
    par = re.findall(r'\)', struct)
    
    print(par)
    return len(par)


# Another Solution: 
# https://py.checkio.org/mission/how-deep/publications/vvm70/python-3/first/share/507c5b5bd42fb11f27fdc3c0dd990da8/

def how_deep(structure):
  pairs = ''.join(filter(lambda x: x in ('(', ')'), str(structure)))
  counter = 0
  while pairs:
    pairs = pairs.replace("()", '')
    counter += 1
  return counter




if __name__ == '__main__':
    print("Example:")
    print(how_deep((1, 2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert how_deep((1, 2, 3)) == 1
    assert how_deep((1, 2, (3,))) == 2
    assert how_deep((1, 2, (3, (4,)))) == 3
    assert how_deep(()) == 1
    assert how_deep(((),)) == 2
    assert how_deep((((),),)) == 3
    assert how_deep((1, (2,), (3,))) == 2
    assert how_deep((1, ((),), (3,))) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")