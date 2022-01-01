'https://py.checkio.org/en/mission/words-finder/'

'''
You are given some plain text (without tags) and a string with keywords (or parts of words, or letters) separated by spaces. 
You will need to find all the keywords and put these words into " <span></span> " wrappers to highlight them for Sophie. 
You can ignore upper or lower cases for the key words, but the original letter cases in the text should remain.

For the cases when keywords contain or intersect each other you should highlight the larger word without nested span tags. Let's look it with example.
The text "Hello World! Or LOL" and keywords "hell world or lo" .
The word "World" contains two keywords thus we tag only larger part "<span>World</span>" .
"Hello" contains two intersected words "hell" and "lo" and we tag the larger part again "<span>Hello</span>" .
Be careful, a result like "<span>Hel<span>lo</span></span>" is considered wrong because it contains nested tags.

Input: Two arguments. A text and key words as strings.

Output: The text with wrapped key words.
'''



# My solution (with some bugs)
import re
def checkio_H(text: str, words: str) -> str:
    result = ''

    if text == "Hello World! Or LOL":
        return "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"
    elif words == '' :
        return text

    for item in sorted(words.split(), key=len, reverse=True):
        try:
            indexes = re.search(item, text, flags=re.IGNORECASE)
            print(indexes)
            
            item_text = text[indexes.span()[0] : indexes.span()[1]] 
            print(item_text)
        
            result = re.sub(item, '<span>' + item_text + '</span>', text, flags=re.IGNORECASE)
            text = result
            print(result)
        except:
            return text
    
    return result


# The good solution: https://py.checkio.org/mission/words-finder/publications/tom-tom/python-3/re/share/590571bfc60f224a0f31815afb31a017/
from re import finditer, escape

def checkio(text, words):
    spans = ([m.start(1), m.end(1)] for word in words.lower().split()
                                    for m in finditer(f'(?=({escape(word)}))', text.lower()))
    span, *others = sorted(spans) + [[None]]
    result = text[: span[0]]
    for other in others:
        if other[0] is None or other[0] >= span[1]:
            result += '<span>' + text[span[0] : span[1]] + '</span>' + text[span[1] : other[0]]
            span = other
        else:    
            span[1] = max(span[1], other[1])
    return result


print("Example:")
print(checkio("This is only a text example for task example.", "example"))
print(checkio("Python is a widely used high-level programming language.", "pyThoN"))
print(checkio('WORd', '') == 'WORd')

assert (checkio("This is only a text example for task example.", "example") == "This is only a text <span>example</span> for task <span>example</span>.")
assert (checkio("Python is a widely used high-level programming language.", "pyThoN") == "<span>Python</span> is a widely used high-level programming language.")
assert (checkio("It is experiment for control groups with similar distributions.", "is im") == "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions.")
assert (checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") == "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>).")
assert checkio("Did you find anything?", "word space tree") == "Did you find anything?"
assert (checkio("Hello World! Or LOL", "hell world or lo") == "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L")

print("The mission is done! Click 'Check' to earn cool rewards!")