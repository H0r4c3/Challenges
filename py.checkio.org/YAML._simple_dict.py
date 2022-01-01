'https://py.checkio.org/en/mission/yaml-simple-dict/'

'''
YAML is a text, and you need to convert it into an object.
The first step is the key-value conversion. The key can be any string consisting of Latin letters and numbers. 
The value can be a single-line string (which consists of spaces, Latin letters and numbers) or a number (int).

I’ll show some examples:

name: John
age: 12
Converted into an object.

{ 
  "name": "John",
  "age": 12
}
'''


import re
def yaml(a):
    a = ' '.join((a.splitlines()))
    
    pattern_keys = re.compile('([\w]+):')
    keys_list = pattern_keys.findall(a)
    #keys_list = list(map(lambda x: int(x) if x.isnumeric() else x, keys_list))
    print(f'pattern_keys: {keys_list}')
    
    #values_list = [item.strip() for item in re.split('name:|age:|class|12:', a)][1:]
    #SEPARATORS = ['name:', 'age:', 'class:', '12:']
    SEPARATORS = list(map(lambda x: x + ':', keys_list))
    pattern_values = re.compile("|".join(SEPARATORS))
    values_list = [item.strip() for item in pattern_values.split(a)][1:]
    print(f'values_list: {values_list}')
    
    values_list = list(map(lambda x: int(x) if x.isnumeric() else x, values_list))
    
    result = dict(zip(keys_list, values_list))
    print(result)
    
    return result


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: John age: 12"""))
    print(yaml("""name: John Fox age: 12 class: 12b"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert yaml("""name: John age: 12""") == {'age': 12, 'name': 'John'}
    assert yaml("""name: John Fox age: 12 class: 12b""") == {'age': 12, 'class': '12b', 'name': 'John Fox'}
    assert yaml("12: 12") == {"12":12}
    assert yaml("""name: Bob Dylan\nburn: 24 May 1941\nresident: Malibu, California, U.S\n\nchildren: 6""") == {"resident":"Malibu, California, U.S","burn":"24 May 1941","name":"Bob Dylan","children":6}
    print("Coding complete? Click 'Check' to earn cool rewards!")