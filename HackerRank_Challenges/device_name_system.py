'Test Toptal - nr. 24'

'''
Create unique device names to be used in... If a device name already exists in the system, an integer number is added at the end of the name to make it unique.
The integer added starts with 1 and is incremented by 1 for each new request of an existing device name. Given a list of device name requests, process
all requests and return an array of the corresponding unique device names.

Example:
n = 6
devicenames = ['switch', 'tv', 'switch', 'tv', 'switch', 'tv']

Return:
uniqueDevicename = ['switch', 'tv', switch1, 'tv1', 'switch2', 'tv2']
'''

def deviceNamesSystem(devicenames):
    uniqueDevicename = []
    
    for item in devicenames:
        i = 0
        if item not in uniqueDevicename:
            uniqueDevicename.append(item)
        else:
            for item_u in uniqueDevicename:
                if item in item_u:
                    i +=1
            item += str(i)
            uniqueDevicename.append(item)
    
    return uniqueDevicename


devicenames = ['switch', 'tv', 'switch', 'tv', 'switch', 'tv']

uniqueDevicename = deviceNamesSystem(devicenames)

print(uniqueDevicename)