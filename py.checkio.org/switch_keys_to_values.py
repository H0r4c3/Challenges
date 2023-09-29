'https://py.checkio.org/en/mission/switch-keys-to-values/share/4853b445fff48638a44a2b57191012ce/'

'''
You are given a dictionary, where keys and values are strings. 
Your function should return a dictionary as well, where keys and values from input dictionary are switched: 
input keys become output values and vice versa.
The only thing left to mention: the values in the result dictionary should be sets (so the input key(s) - the element(s) of the set).
'''

def switch_dict(data: dict[str, str]) -> dict[str, str]:
    keys_of_data = set(data.keys())
    print(keys_of_data)
    values_of_data = set(data.values())
    print(values_of_data)
    
    result = {key:set([item for item in keys_of_data if data[item] == key]) for key in values_of_data}
    #result = {key:set([item for item in set(data.keys()) if data[item] == key]) for key in set(data.values())}
    print(result)
    return result


print("Example:")
#print(switch_dict({"rouses": "red", "car": "red", "sky": "blue"}))

# These "asserts" are used for self-checking
assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
    "red": {"car", "rouses"},
    "blue": {"sky"},
}
assert switch_dict({"1": "one", "2": "two", "3": "one", "4": "two"}) == {
    "one": {"3", "1"},
    "two": {"4", "2"},
}
assert switch_dict({"a": "b", "b": "c", "c": "a"}) == {
    "b": {"a"},
    "c": {"b"},
    "a": {"c"},
}

print("The mission is done! Click 'Check Solution' to earn rewards!")