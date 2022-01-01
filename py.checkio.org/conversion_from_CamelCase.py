'https://py.checkio.org/en/mission/conversion-from-camelcase/'

'''
Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the Python format ("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".

Input: A function name as a CamelCase string.

Output: The same string, but in under_score.
'''

def from_camel_case_(name: str) -> str:
    new_name = name[0].lower() + name[1:]
    
    for item in new_name:
        if item.isupper():
            new_name = new_name.replace(item, '_' + item.lower())
              
    return new_name

import re
def from_camel_case(name: str) -> str:
    name = name[0].lower() + name[1:]
    regex = '([a-z])([A-Z])'
    #print(re.sub(regex, r'\1_\2', name).lower())
    return re.sub(regex, r'\1_\2', name).lower()

if __name__ == '__main__':
    print("Example:")
    #print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"