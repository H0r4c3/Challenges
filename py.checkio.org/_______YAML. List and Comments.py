'https://py.checkio.org/en/mission/yaml-list-and-comments/'

'''
In the 3rd YAML parsing task, we’re going to look into arrays.
'''

import yaml as ya

# Taken from mission YAML. More Types

import re
def yaml(a):
    a = ' '.join((a.splitlines()))
    
    pattern_keys = re.compile('([\w]+):')
    keys_list = pattern_keys.findall(a)
    
    SEPARATORS = list(map(lambda x: x + ':', keys_list))
    pattern_values = re.compile("|".join(SEPARATORS))
    values_list = [item.strip() for item in pattern_values.split(a)][1:]
        
    values_list = [val[1:-1].replace('\\"', '"') if val.startswith('"') and val.endswith('"') 
                   else val.strip('"') if '"' in val 
                   else True if val == 'true' 
                   else False if val == 'false'
                   else None if val in ('null' or not val)
                   else int(val) if val.isnumeric() else val
                   for val in values_list]
    
    #return dict(sorted(list(zip(keys_list, values_list)), key=lambda x: x[0]))
    return dict(list(zip(keys_list, values_list)))


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex "Fox"'}
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


def yaml(a):
    result = ya.load(a, Loader=ya.Loader)
    print(result)
    
    return result


if __name__ == "__main__":
    print("Example:")
    print(yaml('- write some\n- "Alex Chii"\n- 89'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('- write some\n- "Alex Chii"\n- 89') == ["write some", "Alex Chii", 89]
    assert yaml(
        "# comment\n"
        "- write some # after\n"
        "# one mor\n"
        '- "Alex Chii #sir "\n'
        "- 89 #bl"
    ) == ["write some", "Alex Chii #sir ", 89]
    assert yaml("- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5") == [1, 2, 3, 4, 5]
    assert yaml("-\n-\n-\n- 7") == [None, None, None, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")