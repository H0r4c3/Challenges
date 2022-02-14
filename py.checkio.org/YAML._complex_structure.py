'https://py.checkio.org/en/mission/yaml-complex-structure/'

'''
Input: Format string.

Output: An object.
'''

# Best Solution:
# https://py.checkio.org/mission/yaml-complex-structure/publications/kdim/python-3/recursion/share/6e588742db3a7b1d8fe3b1cec602f168/
def convert(value):                                         # return converted
    transform = {'"null"': 'null', '': None, 'null': None,  # value
                 'true': True, 'false': False}              #
    if value in transform:
        return transform[value]
    value = value.replace('\\', '').replace('\"', '"')
    if value[0] == value[-1] == '"':
        value = value[1:-1]
    return int(value) if value.isdigit() else value

def remove_comment(text):                                   # remove comment
    quoted, data = False, ''                                # from line
    for char in text:                                       #
        if char == '"':
            quoted = not quoted
        if char == '#' and not quoted:
            return data
        data += char
    return data

def get_yaml(text):                                         # recursively get yaml
    index = lambda x: len(x) - len(x.lstrip())              # block indent
    ix = index(text[0])                                     #
    (delimeter, result) = ('-', []) if '-' in text[0] else (':', {}) # type of block
    while text:                                             # let's go through the block
        line = text.pop(0)                                  # get line 
        key, value = line.split(delimeter)                  # get key and value
        key, value = key.strip(), convert(value.strip())    # if list then key = ''
        if line.strip()[-1] == delimeter and text and index(text[0]) != ix:
            subtext = []                                    # if find sub-block, go recursively through one
            while text and index(text[0]) != ix:            # get subblock text    
                subtext.append(text.pop(0))                 #
            value = get_yaml(subtext)                       # recursion
        if delimeter == ':':                                #
            result.update({key: value})                     # add value to result
        else:                                               #
            result.append(value)                            #
    return result                                           #

def yaml(a):
    value = [remove_comment(line) for line in a.split('\n') if line and line[0] != '#']
    return get_yaml(value)


if __name__ == '__main__':
    print("Example:")
    print(yaml('- Alex\n'
 '-\n'
 '  - odessa\n'
 '  - dnipro\n'
 '- Li'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('- Alex\n'
 '-\n'
 '  - odessa\n'
 '  - dnipro\n'
 '- Li') == ['Alex', ['odessa', 'dnipro'], 'Li']
    assert yaml('- 67\n'
 '-\n'
 '  name: Irv\n'
 '  game: Mario\n'
 '-\n'
 '- 56') == [67,
 {'game': 'Mario', 'name': 'Irv'},
 None,
 56]
    assert yaml('name: Alex\n'
 'study:\n'
 '  type: school\n'
 '  number: 78\n'
 'age: 14') == {'age': 14,
 'name': 'Alex',
 'study': {'number': 78,
           'type': 'school'}}
    assert yaml('name: Alex\n'
 'study:\n'
 '  - 89\n'
 '  - 89\n'
 '  - "Hell"\n'
 'age: 14') == {'age': 14,
 'name': 'Alex',
 'study': [89, 89, 'Hell']}
    assert yaml('name: Alex\n'
 'study:\n'
 '  -\n'
 '    type: school\n'
 '    num: 89\n'
 '  -\n'
 '    type: school\n'
 '    num: 12\n'
 'age: 14') == {'age': 14,
 'name': 'Alex',
 'study': [{'num': 89,
            'type': 'school'},
           {'num': 12,
            'type': 'school'}]}
    assert yaml('name: Alex\n'
 'study:\n'
 '  -\n'
 '    type: school\n'
 '    nums:\n'
 '      - 12\n'
 '      - 67\n'
 '  -\n'
 '    type: school\n'
 '    num: 12\n'
 'age: 14') == {'age': 14,
 'name': 'Alex',
 'study': [{'nums': [12, 67],
            'type': 'school'},
           {'num': 12,
            'type': 'school'}]}
    print("Coding complete? Click 'Check' to earn cool rewards!")