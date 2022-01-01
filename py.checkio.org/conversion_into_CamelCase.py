'https://py.checkio.org/en/mission/conversion-into-camelcase/'

'''
Your mission is to convert the name of a function (a string) from the Python format (for example "my_function_name") into CamelCase ("MyFunctionName"), where the first char of every word is in uppercase and all words are concatenated without any intervening characters.

Input: A function name as a string.

Output: The same string, but in CamelCase.
'''

import re
def to_camel_case_(name: str) -> str:
    print(name)
    regex = '([A-Z])([a-z])'
    name = re.sub(regex, 'r\1\_2', name).capitalize()
    print(name)
    return name


def to_camel_case(name: str) -> str:
    #name_list = [item.capitalize() for item in name.split('_')]
    #name = ''.join(name_list)
    #return name
    return ''.join([item.capitalize() for item in name.split('_')])


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"