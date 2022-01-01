'https://py.checkio.org/en/mission/flatten-dict/'

'''
You are given a dictionary where the keys are strings and the values are strings or dictionaries. 
The goal is flatten the dictionary, but save the structures in the keys. The result should be the a dictionary without the nested dictionaries. 
The keys should contain paths that contain the parent keys from the original dictionary. 
The keys in the path are separated by a "/". 
If a value is an empty dictionary, then it should be replaced by an empty string ("").
'''

def flatten(dictionary, parent_key='', sep='/'):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + sep + key if parent_key else key
        if value and isinstance(value, dict):
            items.extend(flatten(value, new_key, sep=sep).items())
        elif value == {}: 
            items.append((new_key, ""))
        else:
            items.append((new_key, value))
            
    #print(dict(items))
    return dict(items)



# NOK for value = {}
import pandas as pd    
def flatten(dictionary):
    result = dict()
    
    for key, value in dictionary.items():
        if value == {}:
            dictionary[key] = ""
    print(dictionary)
    
    df = pd.json_normalize(dictionary, errors='ignore', sep='/')
    result = df.to_dict(orient='index')[0]
    
    print(result)
    return result



if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')