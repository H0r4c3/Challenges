'https://py.checkio.org/en/mission/friendly-number/'

'''
You should write a function for converting a number to string using several rules. 
First of all, you will need to cut the number with a given base ( base argument; default 1000). 
The value is a float number with decimal after the point ( decimals argument; default 0). 
For the value, use the rounding towards zero rule (5.6⇒5, -5.6⇒-5) if the decimal = 0, otherwise use the standard rounding procedure. 
If the number of decimals is greater than the current number of digits after dot, trail value with zeroes. 
The number should be a value with letters designating the power. You will be given a list of power 
designations ( powers argument; default ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']). If you are given suffix ( suffix argument; default ‘’) , 
then you must append it. If you don’t have enough powers - stay at the maximum. And zero is always zero without powers, but with suffix.
'''

# https://github.com/narimiran/checkio/blob/master/friendly-number.py

from decimal import Decimal

def friendly_number(
    number,
    base=1000,
    decimals=0,
    suffix="",
    powers=["", "k", "M", "G", "T", "P", "E", "Z", "Y"],
):
    """
    Format a number as friendly text, using common suffixes.
    """
    
    number = Decimal(number)
    power = 0
    
    while abs(number) >= base and power < len(powers)-1:
        power += 1
        number /= base
    number = round(number, decimals) if decimals else int(number)

    print('{:.{dec}f}{}{}'.format(number, powers[power], suffix, dec=decimals))
    return '{:.{dec}f}{}{}'.format(number, powers[power], suffix, dec=decimals)


# Another Solution:
# https://py.checkio.org/mission/friendly-number/publications/gyahun_dash/python-3/second/?ordering=most_voted&filtering=all
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):

    exponents = [e for e in range(len(powers)) if base**e <= abs(number)]
    exponent = max(exponents) if exponents != [] else 0

    divided = number / base**exponent
    approx = round(divided, decimals) if decimals > 0 else int(divided)

    return '{:.{}f}{}{}'.format(approx, decimals, powers[exponent], suffix)
    
    


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert friendly_number(102) == "102", "102"
    assert friendly_number(10240) == "10k", "10k"
    assert friendly_number(12341234, decimals=1) == "12.3M", "12.3M"
    assert friendly_number(12461, decimals=1) == "12.5k", "12.5k"
    assert friendly_number(1024000000, base=1024, suffix="iB") == "976MiB", "976MiB"
    print('Done!')