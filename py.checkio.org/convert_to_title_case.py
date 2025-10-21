'https://py.checkio.org/en/mission/convert-to-title-case/'

'''
Your function should take a string as an input and convert all the first letters of the words in the string to uppercase, 
making the string a title case (other letters must be in lowercase).
'''

def to_title_case(sentence: str) -> str:
    sentence_list = sentence.split()
    sentence_list_cap = [word.capitalize() for word in sentence_list]
    sentence_result = ' '.join(sentence_list_cap)
    
    print(sentence_result)
    return sentence_result


# BEST Solution: 
# https://py.checkio.org/mission/convert-to-title-case/publications/faccanoni/python-3/to_title_case/?ordering=most_voted&filtering=all
def to_title_case(sentence: str) -> str:
    return sentence.title()


print("Example:")
print(to_title_case("hello world"))

# These "asserts" are used for self-checking
assert to_title_case("hello world") == "Hello World"
assert to_title_case("openai gpt-4") == "Openai Gpt-4"
assert to_title_case("this is a title") == "This Is A Title"
assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"
assert to_title_case("JUMPs ovER a LAZy dog") == "Jumps Over A Lazy Dog"
assert to_title_case("typescript is great") == "Typescript Is Great"
assert to_title_case("the answer is 42") == "The Answer Is 42"
assert to_title_case("to be or not to be") == "To Be Or Not To Be"
assert to_title_case("that is the question") == "That Is The Question"
assert to_title_case("") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")