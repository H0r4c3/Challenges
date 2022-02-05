'https://py.checkio.org/en/mission/currency-style/'

'''
Many countries use different conventions for the thousands separator and decimal mark.

Only currency amounts in dollars should be converted: $1.234,50 to $1,234.50, $1.000 to $1,000, and $4,57 to $4.57
'''
import ipaddress
def checkio(line: str) -> str:
    
    # check if line is an IP address
    try:
        ip = ipaddress.ip_address(line)
        return line
    except ValueError:
        pass
    
    result_list = list()
    result = line.replace('.', ',')
    
    def replacing(result):
        for item in result:
            if item == '':
                result_list.append(item)
                continue
            if item[-1] != ',':
                if len(item) > 3 and item[-3] == ',':
                    item1 = item[:-3] + '.' + item[-2:]
                    result_list.append(item1)
                else:
                    result_list.append(item)
            
            elif item[-1] == ',':
                item1 = item[:-1] + '.'
                if len(item1) > 4 and item1[-4] == ',':
                    item2 = item1[:-4] + '.' + item1[-3:]
                    result_list.append(item2)
                else:
                    result_list.append(item1)
        
        return result_list
    
    result = result.split(' ')
    result = replacing(result)
    result_string = ' '.join(result_list)
       
    print(result_string)
    return result_string




# Best Solution: https://py.checkio.org/mission/currency-style/publications/Sim0000/python-3/first/?ordering=most_voted&filtering=all
import re
def checkio(text):
    reform = lambda match: match.group(0).translate(str.maketrans(',.', '.,'))
    return re.sub('\$\d{1,3}(\.\d{3})*(,\d{2}){,1}(?!\d)', reform, text)

# \$            letter '$'
# \d{1,3}       [0-9] of length {1, 3}
# (\.\d{3})*    repetition of \.[0-9]{3}, if exists
# (,\d{2}){,1}  ,[0-9]{2}, if exists
# (?!\d)        no [0-9] after pattern




# Best Solution: https://py.checkio.org/mission/currency-style/publications/kurosawa4434/python-3/first/share/2a7cb835fc4f3d7104853f3bfcee0e18/
from re import search, sub
def checkio_(text):
    
    def rep_func(match_obj):
        money = match_obj.group(0)
        if not search('\.[0-9]{3}', money) and not search(',[0-9]{2}$', money):
            return money
        return money.translate(str.maketrans(".,", ",."))

    return sub('\$[^ ]+[0-9]', rep_func, text)



if __name__ == '__main__':
    print("Example:")
    #print(checkio('$5.34'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('$5.34') == '$5.34', 'US Style'
    assert checkio('$5,34') == '$5.34'
    assert checkio('$222,100,455.34') == '$222,100,455.34', 'US Style'
    assert checkio('$222.100.455,34') == '$222,100,455.34'
    assert checkio('$222,100,455') == '$222,100,455'
    assert checkio('$222.100.455') == '$222,100,455'
    assert checkio("$4,13 + $5,24 = $9,37") == "$4.13 + $5.24 = $9.37"
    assert checkio("$4.545,45 is less than $5,454.54.") == "$4,545.45 is less than $5,454.54."
    assert checkio("127.255.255.255") == "127.255.255.255"
    assert checkio("Clayton Kershaw $31.000.000\nZack Greinke   $27.000.000\nAdrian Gonzalez $21.857.143\n") == "Clayton Kershaw $31,000,000\nZack Greinke   $27,000,000\nAdrian Gonzalez $21,857,143\n"
    print("Coding complete? Click 'Check' to earn cool rewards!")