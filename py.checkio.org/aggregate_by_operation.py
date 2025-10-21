'https://py.checkio.org/en/mission/aggregate-by-operation/'

'''
You are given a list of tuples. Each tuple consists of two values: a string and an integer. 
You need to create and return a dictionary, where keys are string values (except the first character) from input tuples. 
Values are aggregated integer values from input tuples for each specific key. 
Each aggregating operation must be done according to the operation sign - the first character of string key. 
Division by zero should be ignored. The resulted dictionary should not include items with empty key or zero value.
'''

def verification(result):
    '''Check that the key is not an empty string and the value is not 0'''
    result = {key:value for key, value in result.items() if key and value}
    
    return result

def convert_tuples(data):
    '''Move the sign from key to value'''
    data_new = list()
    for item in data:
        oper = item[0][0]
        number = item[1]
        #item[0] = item[0][1:]
        #item[1] = sign + str(number)
        if oper == '/' and number == 0:
            pass
        else:
            data_new.append((item[0][1:], oper + str(number)))
            
    return data_new

def concatenation(my_list):
    print(my_list)
    concat = ''.join(my_list)
    print(f'concat = {concat}')
    eq_pos = concat.rfind('=')
    print(f'eq_pos = {eq_pos}')
    if eq_pos != -1:
        concat = concat[eq_pos+1:]
    if concat == '*0':
        concat = 0
    else:
        concat = eval(concat)
    print(concat)
    
    return concat


def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    print(f'START: data is {data}')
    data_dict = dict()
    result = dict()
    
    data_new = convert_tuples(data)
    print(data_new)
    
    for key, value in data_new:
        data_dict.setdefault(key, []).append(value)
    print(f'data_dict = {data_dict}')
        
    result = {key : concatenation(value) for key, value in data_dict.items()}
    print(f'result after concatenation = {result}')
    
    result = verification(result)
    print(f'result = {result}')
    
    return result

# BEST Solution:
#https://py.checkio.org/mission/aggregate-by-operation/publications/ssk8/python-3/first/?ordering=most_voted&filtering=all

from collections import defaultdict as dd


def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    data_dict = dd(int)
    for k, v in data:
        op, k = k[0], k[1:]
        match op, bool(v):
            case "+", Any: data_dict[k] += v
            case "-", Any: data_dict[k] -= v
            case "*", Any: data_dict[k] *= v
            case "/", True: data_dict[k] /= v
            case "=", Any: data_dict[k] = v
        if not data_dict[k] or not k: del(data_dict[k])
    return data_dict



# BEST Solution:
# https://py.checkio.org/mission/aggregate-by-operation/publications/tokiojapan55/python-3/first/?ordering=most_voted&filtering=all

def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    r = dict()
    for key, v in data:
        k, op = key[1:], key[0]
        if op == '=':
            r[k] = v
        else:
            try: r[k] = eval(str(r.get(k, 0)) + op + str(v))
            except: pass
    return {k:r[k] for k in r if r[k] and len(k)}


print("Example:")
#print(aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]))

# These "asserts" are used for self-checking
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}
assert aggr_operation([('+a', 5), ('*a', 6), ('/a', 3), ('=a', 3)]) == {'a': 3}
assert aggr_operation([('+a', 0), ('*b', 0), ('+', 35)]) == {}

print("The mission is done! Click 'Check Solution' to earn rewards!")

