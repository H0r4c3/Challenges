'https://py.checkio.org/en/mission/text-formatting/'

'''
You are given a long line (a monospace font), and you have to break the line in order to respect a given width. 
Then you have to format the text according to the given style: 'l' means you have to align the text to the l eft, 'c' for c enter, 'r' for r ight, and 'j' means 
you have to j ustify the text. Finally, the parts of the output shouldn’t end with a whitespace.

If you have to put 2 * n + 1 spaces around a line in order to center it, then put n spaces before, not n + 1.

The justification rules:

Since we can't always put the same number of spaces between words in a line, put big blocks of spaces first. For example: X---X---X--X--X--X when you 
have to put 12 spaces in 5 gaps: 3-3-2-2-2.
Don't justify the last line of a text.
You won't have to consider splitting a word into two parts because the given widths are big enough.

Input: A text (string), width (integer) and style (string).

Output: The formatted text (string).
'''

# # This solution is incomplete!!!!!
# def text_formatting_(text: str, width: int, style: str) -> str:
#     print(text)
#     parts = [text[i:i+width] for i in range(0, len(text), width)]
#     print(parts)
    
#     result = '\n'.join(parts)
    
#     print(result)
#     return '\n'.join(parts)


# My Solution:
import textwrap
def text_formatting(text: str, width: int, style: str) -> str:
    print(text)
    parts = textwrap.wrap(text, width)
    print(parts)
    
    if style == 'l':
        return '\n'.join(parts)
    if style == 'c':
        return '\n'.join(' '*((width-len(line))//2) + line for line in parts)
    if style == 'r':
        return '\n'.join(line.rjust(width) for line in parts)
    
    for i in range(len(parts) - 1):
        gap, big_blocks = divmod(width - len(parts[i]), parts[i].count(' '))
        parts[i] = parts[i].replace(' ', ' '*(gap+1)).replace(' '*(gap+1), ' '*(gap+2), big_blocks)
    return '\n'.join(parts)



# Best Solution:
# https://py.checkio.org/mission/text-formatting/publications/kurosawa4434/python-3/first/share/80998fc283f2c542bbc107255646ef61/
def text_formatting_(text: str, width: int, style: str) -> str:

    def make_row(text):
        rest = text.split()
        row = []
        while rest:
            word = rest.pop(0)
            if len(' '.join(row + [word])) > width:
                yield ' '.join(row), False
                row.clear()
            row.append(word)
        yield ' '.join(row), True

    def justify(row, width):
        q, r = divmod(width-len(row), row.count(' '))
        return ''.join(' '*(1+q+(i <= r))*(i > 0)+w for i, w in enumerate(row.split(' ')))

    result = []
    fn = {'r': str.rjust, 'l': str.ljust, 'c': str.center, 'j': justify}

    for row, last in make_row(text):
        if style == 'j' and last:
            style = 'l'
        result.append(fn[style](row, width).rstrip())

    return '\n'.join(result)


# Best Solution: 
# https://py.checkio.org/mission/text-formatting/publications/David_Jones/python-3/textwrapwrap/?ordering=most_voted&filtering=all
from textwrap import wrap

def text_formatting(text, width, style):
    parts = wrap(text, width=width)
    if style == 'l':
        return '\n'.join(parts)
    if style == 'c':
        return '\n'.join(' '*((width-len(line))//2) + line for line in parts)
    if style == 'r':
        return '\n'.join(line.rjust(width) for line in parts)
    for i in range(len(parts) - 1):
        gap, big_blocks = divmod(width - len(parts[i]), parts[i].count(' '))
        parts[i] = parts[i].replace(' ', ' '*(gap+1)) \
                           .replace(' '*(gap+1), ' '*(gap+2), big_blocks)
    return '\n'.join(parts)


# Best Solution: 
# https://py.checkio.org/mission/text-formatting/publications/veky/python-3/left-because-center-justification-wasnt-right/?ordering=most_voted&filtering=all

def text_formatting(text, width, style):
    
    def parts(words):
        line = next(words)
        for word in words:
            old_line = line
            line += ' ' + word
            if len(line) > width:
                yield old_line, False
                line = word
        yield line, True
    
    def interleave(line):
        words = line.split()
        n = len(words) - 1
        q, r = divmod(width - len(line), n)
        for word, space in zip(words, [' '*(q+1)]*r + [' '*q]*(n-r)):
            yield word + ' ' + space
        yield words[~0]
    
    def align(line):
        if style == 'l': return line
        elif style == 'r': return line.rjust(width)
        elif style == 'c': return format(line, f'^{width}').rstrip()
        elif style == 'j': return ''.join(interleave(line))            
    
    def aligned():
        for line, last in parts(iter(text.split())):
            if last and style == 'j': yield line
            else: yield align(line)
            
    return '\n'.join(aligned())



if __name__ == '__main__':
    LINE = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure '
            'harum suscipit aperiam aliquam ad, perferendis ex molestias '
            'reiciendis accusantium quos, tempore sunt quod veniam, eveniet '
            'et necessitatibus mollitia. Quasi, culpa.')

    print('Example:')
    #print(text_formatting(LINE, 38, 'l'))

    assert text_formatting(LINE, 38, 'l') == \
        '''Lorem ipsum dolor sit amet,
consectetur adipisicing elit. Iure
harum suscipit aperiam aliquam ad,
perferendis ex molestias reiciendis
accusantium quos, tempore sunt quod
veniam, eveniet et necessitatibus
mollitia. Quasi, culpa.''', 'Left 38'

    assert text_formatting(LINE, 30, 'c') == \
        ''' Lorem ipsum dolor sit amet,
consectetur adipisicing elit.
 Iure harum suscipit aperiam
  aliquam ad, perferendis ex
     molestias reiciendis
accusantium quos, tempore sunt
   quod veniam, eveniet et
   necessitatibus mollitia.
        Quasi, culpa.''', 'Center 30'

    assert text_formatting(LINE, 50, 'r') == \
        '''           Lorem ipsum dolor sit amet, consectetur
     adipisicing elit. Iure harum suscipit aperiam
   aliquam ad, perferendis ex molestias reiciendis
       accusantium quos, tempore sunt quod veniam,
 eveniet et necessitatibus mollitia. Quasi, culpa.''', 'Right 50'

    assert text_formatting(LINE, 45, 'j') == \
        '''Lorem   ipsum  dolor  sit  amet,  consectetur
adipisicing elit. Iure harum suscipit aperiam
aliquam    ad,   perferendis   ex   molestias
reiciendis  accusantium  quos,  tempore  sunt
quod   veniam,   eveniet   et  necessitatibus
mollitia. Quasi, culpa.''', 'Justify 45'

print('Done!')