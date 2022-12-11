'https://py.checkio.org/en/mission/simplify-unix-path/'

'''
You can think about it as simplifying of the first argument "cd" command (a standard bash command). Simplifying means making shorter.

For instance if I do cd a/../b it works the same as cd b . Which means "b" is simplifying of "a/../b". It is much easier to explain everything using examples.

Input: String. Non-Empty valid unix path.

Output: String. Unix path.
'''

import re

def simplify_path(path):
    new_path = ''
    
    while path != new_path:
        new_path = path
        
        path=re.sub(r'(?<!^)/(?=$)', '', path)
        path=re.sub(r'/\.(?=/|$)', '', path)
        path=re.sub(r'//', '/', path)
        path=re.sub(r'^[^/.]+?/\.\.', '.', path)
        path=re.sub(r'/[^/.]+?/\.\.', '', path)
        path=re.sub(r'^\./', '', path)
        path=re.sub(r'^/\.\.(?=/|$)', '/', path)
        
    print(path)    
    return path


# Best Solution: 
# https://py.checkio.org/mission/simplify-unix-path/publications/sawako.oono/python-3/first/?ordering=most_voted&filtering=all

import re

def simplify_path_(path):
    compair = ""
    while path != compair:
        compair=path
        path=re.sub(r"(?<!^)/(?=$)","",path)
        path=re.sub(r"/\.(?=/|$)","",path)
        path=re.sub(r"//","/",path)
        path=re.sub(r"^[^/.]+?/\.\.",".",path)
        path=re.sub(r"/[^/.]+?/\.\.","",path)
        path=re.sub(r"^\./","",path)
        path=re.sub(r"^/\.\.(?=/|$)","/",path)
    return path

# Another Best Solution: 
# https://py.checkio.org/mission/simplify-unix-path/publications/veky/python-3/pass/?ordering=most_voted&filtering=all

def simplify_path_(path):
    segments = path.split('/')
    absolute = not segments[0]
    result = []
    for segment in segments:
        if '.'.startswith(segment): pass
        elif segment != '..': result.append(segment)
        elif result and result[~0] != '..': del result[~0]
        elif not absolute: result.append(segment)            
    return '/'*absolute + '/'.join(result) or '.'


# Another Best Solution: 
# https://py.checkio.org/mission/simplify-unix-path/publications/kdim/python-3/regex-in-loops-8-lines/?ordering=newest&filtering=all

import re
def simplify_path_(path):
    '''
    //, /./, /.$, /../, /..$  --> /
    abc/$                     --> abc
    abc/..                    --> .
    ^./                       --> ''
    all it in loop
    '''
    
    p, t = '', {r'//|/\.(/|$)|^/\.\.($|/)': r'/', r'(.+)/$': r'\1', r'\w+/\.\.': r'.', r'^\./': r''}
    while p != path:
        p = path
        for i, j in t.items():
            path = re.sub(i, j, path)
    return path



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # last slash is not important
    assert simplify_path('/a/') == '/a'

    # double slash can be united in one
    assert simplify_path('/a//b/c') == '/a/b/c'

    # double dot - go to previous folder
    assert simplify_path('dir/fol/../no') == 'dir/no'
    assert simplify_path('dir/fol/../../no') == 'no'

    # one dot means current dir
    assert simplify_path('/a/b/./ci') == '/a/b/ci'
    assert simplify_path('vi/..') == '.'
    assert simplify_path('./.') == '.'

    # you can't go deeper than root folder
    assert simplify_path('/for/../..') == '/'
    assert simplify_path('/for/../../no/..') == '/'

    # not all double-dots can be simplified in related path
    assert simplify_path('for/../..') == '..'
    assert simplify_path('../foo') == '../foo'
    
    # replace ./ with .
    assert simplify_path('./') == '.'
    
    #
    assert simplify_path("//./") == '/'
    
    print('Simply enough! Let\'s check it now!!')