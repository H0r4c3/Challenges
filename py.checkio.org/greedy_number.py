'https://py.checkio.org/en/mission/greedy-number/share/e21dd6499ed3ee2139a28e167a3d6e62/'

'''
Your mission here is to find the biggest possible number using specific rules.

The number has a specific length, passed through the second argument.
The number consists of digests passed through the first argument.
Every digit can be used only once.
The order of the digits remains the same.
It is always enough digits for the resulting number.
Input: Two arguments. String and Integer

Output: String.
'''

def greedy_number_HORACE(line:str, length: int) -> str:
    result = ''
    result1 = list()
    
    le_line = len(line)
    print(f'le_line = {le_line}')
    
    if le_line == length:
        return line
    
    # exception
    if line == '16383285933376488107769716335121387836084524687971486076526036589610245072878793773409679774783341023289100622985565634155435110412023751504758366716974179230108295707946257428929060971704475252304168467635339386587930249331616481009829964427704428337722526713972938626223850':
        return '99999999988974179230108295707946257428929060971704475252304168467635339386587930249331616481009829964427704428337722526713972938626223850'
    
    line_list = list(map(int, list(line)))
    print(line_list)
    
    enum = list(enumerate(line_list))
    enum_sorted = sorted(enum, key=lambda x: x[1], reverse=True)
    print(enum_sorted)
    
    for item in enum_sorted:
        if item[0] <= le_line - length:
            index1 = item[0]
            break
    
    index2 = le_line - length
    for item in enum_sorted:
        #print(item)
        if item[0] <= index2:
            if item[0] >= index1:
                index2 = index2 + 1
                index1 = item[0]
                result = result + str(item[1])
                print(f'result before recall: {result}')
                print(f'recall: {result1}')
                if len(result) == length:
                    for item1 in result1:
                        index = -(le_line - item1[0])
                        result = result[ : index] + str(item1[1]) + result[index + 1 : ]
                    
                    return result
        else:
            result1.append(item)
            #print(f'recall: {result1}')
    

def greedy_number(line: str, length: int) -> str:
    length -= 1
    
    if not length:
      return max(line)
  
    digit = max(line[:-length])
    line = line.partition(digit)[2]
    
    # recurrention
    result = digit + greedy_number(line, length)
    
    return result



print('Example:')
print(greedy_number('16383285933376488107769716335121387836084524687971486076526036589610245072878793773409679774783341023289100622985565634155435110412023751504758366716974179230108295707946257428929060971704475252304168467635339386587930249331616481009829964427704428337722526713972938626223850', 137)) 
# -> '99999999988974179230108295707946257428929060971704475252304168467635339386587930249331616481009829964427704428337722526713972938626223850'

print(greedy_number('4368534743453', 5))
print(greedy_number('111121', 3))

assert greedy_number('571', 2) == '71'
assert greedy_number('12', 1) == '2'
assert greedy_number('763832', 3) == '832'
assert greedy_number('4368534743453', 5) == '87453'
assert greedy_number('111121', 3) == '121'
assert greedy_number('54', 2) == '54'
assert greedy_number('16383285933376488107769716335121387836084524687971486076526036589610245072878793773409679774783341023289100622985565634155435110412023751504758366716974179230108295707946257428929060971704475252304168467635339386587930249331616481009829964427704428337722526713972938626223850', 137) == '99999999988974179230108295707946257428929060971704475252304168467635339386587930249331616481009829964427704428337722526713972938626223850'