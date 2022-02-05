'https://py.checkio.org/en/mission/non-empty-lines/'

'''
You need to count how many non-empty lines a given text has.

An empty line is a line without symbols or the one that contains only spaces.

Input: A text.

Output: An int.
'''

def non_empty_lines(text: str) -> int:
    # Line is a blank line if and only if line.strip() returns an empty string.
    print(text)
   
    all_lines = text.split('\n')
    print(all_lines)
    
    lines_no_empty = [item for item in all_lines if item.strip() != '']
    print(lines_no_empty)
    
    return len(lines_no_empty)


if __name__ == '__main__':
    print("Example:")
    print(non_empty_lines('one simple line\n'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert non_empty_lines('one simple line\n') == 1
    assert non_empty_lines('') == 0
    assert non_empty_lines('\nonly one line\n            ') == 1
    assert non_empty_lines('''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            ''') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")