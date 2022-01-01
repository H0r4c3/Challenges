'https://py.checkio.org/en/mission/yaml-more-types/'

'''
This is the second task on parsing YAML. It represents the next step where parsing gets more complicated. 
The data types, such as null and bool, are being added, and besides that, you’re getting the ability to use quotes in strings.

Here are some of the examples:

name: "Bob Dylan"
children: 6
{
  "name": "Bob Dylan", 
  "children": 6
}
As you can see, the string can be put in quotes. It can be both double and single quotes.
'''

import re
def yaml(a):
    a = ' '.join((a.splitlines()))
    print(f'a = {a}')
    
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
        
    values_list = [val[1:-1].replace('\\"', '"') if val.startswith('"') and val.endswith('"') 
                   else val.strip('"') if '"' in val 
                   else True if val == 'true' 
                   else False if val == 'false'
                   else None if val in ('null' or not val)
                   else int(val) if val.isnumeric() else val
                   for val in values_list]
        
    print(f'values_list after replacings: {values_list}')
    
    #values_list = list(map(lambda x: int(x) if x.isnumeric() else x, values_list))
    
    result = dict(sorted(list(zip(keys_list, values_list)), key=lambda x: x[0]))
    print(f'result = {result}')
    
    return result







# https://py.checkio.org/mission/yaml-more-types/publications/twilyght/python-3/first/share/91319ff3d782536f4df357db91284d55/
def yaml_OK(a):
    BOOLS = ['false', 'true']
    
    obj = {}
    for line in a.splitlines():
        split_index = line.find(':')
        if split_index != -1:
            name, val_str = line[:split_index].strip(), line[split_index + 1:].strip()
            if val_str.startswith('"') and val_str.endswith('"'):
                value = val_str[1:-1].replace('\\"', '"')
            elif val_str in BOOLS:
                value = bool(BOOLS.index(val_str))
            elif val_str.isdigit():
                value = int(val_str)
            elif val_str == 'null' or not val_str:
                value = None
            else:
                value = val_str
            obj[name] = value
    return obj





if __name__ == '__main__':
    print("Example:")
    print(yaml('name: John\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert yaml('name: John\nage: 12') == {'age': 12, 'name': 'John'}
    assert yaml('name: John Fox\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'John Fox'}
    assert yaml('name: "John Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'John Fox'}
    assert yaml('name: "John \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'John "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'alive: false') == {'alive': False,
     'children': 6,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding:') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: null') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: "null" ') == {'children': 6,
     'coding': 'null',
     'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")