'https://py.checkio.org/en/mission/convert-and-aggregate/'

'''
You are given a list of tuples. Each tuple consists of two values: a string and an integer. 
You need to create and return a dictionary, where keys are string values from input tuples and values are 
aggregated (summed) integer values from input tuples for each specific key. 
The resulted dictionary should not include items with empty key or zero value.
'''

def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    data_dict = dict()
    
    for key, value in data:
        if key in data_dict.keys():
            print(f'Key {key} does exist in dictionary')
            data_dict[key] += value
        else:
            print(f'Key {key} does not exist in dictionary')
            data_dict[key] = value
    
    # Check that the key is not an empty string and the value is not 0
    data_dict = {key:value for key, value in data_dict.items() if key and value}
            
    print(data_dict)
    return data_dict


print("Example:")
#print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")