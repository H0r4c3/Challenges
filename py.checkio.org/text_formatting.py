'https://py.checkio.org/en/mission/text-formatting/'

'''
You are given a long line (a monospace font), and you have to break the line in order to respect a given width. 
Then you have to format the text according to the given style: 'l' means you have to align the text to the l eft, 'c' for c enter, 'r' for r ight, and 'j' means 
you have to j ustify the text. Finally, the lines of the output shouldn’t end with a whitespace.

If you have to put 2 * n + 1 spaces around a line in order to center it, then put n spaces before, not n + 1.

The justification rules:

Since we can't always put the same number of spaces between words in a line, put big blocks of spaces first. For example: X---X---X--X--X--X when you 
have to put 12 spaces in 5 gaps: 3-3-2-2-2.
Don't justify the last line of a text.
You won't have to consider splitting a word into two parts because the given widths are big enough.

Input: A text (string), width (integer) and style (string).

Output: The formatted text (string).
'''

def text_formatting(text: str, width: int, style: str) -> str:
    return text


if __name__ == '__main__':
    LINE = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure '
            'harum suscipit aperiam aliquam ad, perferendis ex molestias '
            'reiciendis accusantium quos, tempore sunt quod veniam, eveniet '
            'et necessitatibus mollitia. Quasi, culpa.')

    print('Example:')
    print(text_formatting(LINE, 38, 'l'))

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