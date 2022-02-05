'https://py.checkio.org/en/mission/ip-network-route-summarization/'

'''
A will convert these IP addresses to binary format, align them and find the boundary line between the 
common prefix on the left (highlighted in red), and the remaining bits on the right.

A creates a new IP address made of the common bits, and all other bits set to "0".
This new IP address is converted back to decimal numbers.
Finally, A computes the number of common bits, also called "subnet".
'''

import ipaddress
from itertools import takewhile
from os import path
def checkio(data):
    # convert the IP addresses to binary format
    #ip_bin = [bin(int(ipaddress.IPv4Address(item)))[2:] for item in data]
    ip_bin = [''.join("{:08b}".format(int(i)) for i in ip.split('.')) for ip in data]
    print(ip_bin)
    
    # find the common prefix (another method, but not accepted on the checkio site)
    #common_prefix = path.commonprefix(ip_bin)

    char_tuples = zip(*ip_bin)
    #print(list(char_tuples))
    prefix_tuples = takewhile(lambda x : all(x[0] == y for y in x), char_tuples)
    #print(list(prefix_tuples))
    common_prefix = ''.join(x[0] for x in prefix_tuples)
    print(f'common_prefix = {common_prefix}')
    
    # calculate the subnet (number of common bits)
    subnet = len(common_prefix)
    print(len(common_prefix))
    
    # fill the uncommon part with 0
    new_ip_bin = common_prefix.ljust(32, '0')
    
    # convert the binary format to IP format
    new_ip = str(ipaddress.ip_address(int(new_ip_bin, 2)))
    
    # add the subnet to the new IP address
    result = new_ip + '/' + str(subnet)
    print(result)
    
    return result




# Best Solution: https://py.checkio.org/mission/ip-network-route-summarization/publications/CDG.Axel/python-3/4-lines/?ordering=most_voted&filtering=all

def checkio_(data):
    """
        1. Transform list to binary ip
        2. Find first position when symbols different (idx)
        3. Form mask started from same digits then zeros
        4. Return mask in ip form and idx
    """
    lst = [''.join(f'{int(d):08b}' for d in ip.split('.')) for ip in data]
    idx = next((j for j, e in enumerate(1 == len(set(i)) for i in zip(*lst)) if not e), 32)
    mask = lst[0][:idx] + '0' * (32-idx)
    return f"{'.'.join(str(int(mask[i*8:(i+1)*8], 2)) for i in range(4))}/{idx}"




# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert (
        checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"])
        == "172.16.12.0/22"
    ), "First Test"
    assert (
        checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"
    ), "Second Test"
    assert (
        checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"])
        == "128.0.0.0/2"
    ), "Third Test"
    
    assert checkio(["10.1.57.0","10.1.59.0","10.1.61.0"]) == "10.1.56.0/21"
    assert checkio(["172.16.14.0","172.16.17.0","172.16.25.0","10.1.57.0","10.1.59.0","10.1.61.0"]) == "0.0.0.0/0"
    
    print('Done!')