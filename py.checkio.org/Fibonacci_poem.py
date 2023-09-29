'https://py.checkio.org/en/mission/fibonacci-poem/share/36a9a5788fd360c30b9c3a7469703972/'

'''
Split a given text into multiline one with "\n", where each line includes number of words equal to the current Fibonacci number.
'''

from functools import lru_cache

@lru_cache(maxsize = 128)
def calc_fibo(n):
    if n < 2:
        return n
    
    elem = calc_fibo(n-1) + calc_fibo(n-2)

    return elem
    
    
def fibo_poem(text: str) -> str:
    if text == '':
        return ''
    
    fibo = list()
    
    words = text.split()
    print(words, len(words))
    
    line = 1
    start_word = 0
    end_word = 0
    result = ''
    line_list = list()
    
    while end_word < len(words):
        current_line_length = calc_fibo(line)
        end_word += current_line_length
        this_line = words[start_word:end_word]
        this_line_to_print = ' '.join(this_line)
        #print(this_line_to_print)
        line_list.append(this_line_to_print + '\n')
        #print(line_list)
        line = line + 1
        start_word += current_line_length
    
    last_elem = line_list[-1]
    len_last = last_elem.count(' ') + 1
    diff = current_line_length - len_last
    last_elem = last_elem[0:-1] + (' _' * diff)
    line_list = line_list[0:-1]
    line_list.append(last_elem)
    print(line_list)
    result = ''.join(line_list)
        
    print(result)
    return result


# Best Solution: https://py.checkio.org/mission/fibonacci-poem/publications/kdim/python-3/first/?ordering=most_voted&filtering=all#comment-118979

def fibo_poem(text: str) -> str:
    a, b, text, poem = 0, 1, text.split(), []
    while text:
        row, text = text[:b], text[b:]
        row.extend('_' * (b - len(row)))
        poem.append(' '.join(row))
        a, b = b, a + b
    return '\n'.join(poem)



print("Example:")
print(fibo_poem("Zen of Python"))

# These "asserts" are used for self-checking
assert fibo_poem("") == ""
assert fibo_poem("Django framework") == "Django\nframework"
assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
assert (
    fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
    == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
)

print("The mission is done! Click 'Check Solution' to earn rewards!")