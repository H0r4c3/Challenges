'https://py.checkio.org/en/mission/restricted-sum/'

'''
Given a list of numbers, you should find the sum of these numbers. 
Your solution should not contain any of the banned words, even as a part of another word.

The list of banned words are as follows:

sum
import
for
while
reduce
Input: A list of numbers.

Output: The sum of numbers.
'''

        
def checkio(data, my_sum=0): 
    if not data: 
        return my_sum 
    else: 
        return checkio(data, data.pop() + my_sum)
    
    
# Another Solution (using 'StopIteration')
def checkio(data, my_sum=0):
    x = iter(data)
    try:
        for i in range(len(data)):
            print(x.__next__())
            my_sum += x.__next__()
        
    except StopIteration as e:
        print("StopIteration error handled successfully")
        return my_sum
        
    



# Best Solutions: 
# https://py.checkio.org/mission/restricted-sum/publications/Bartek.Knobel/python-3/first/share/7ccb64aa3a5f25eee6c04da9b9d6a1a9/

def checkio_(data):
      if not data:
        return 0
      return data[0] + checkio(data[1:])


if __name__ == "__main__":
    assert checkio([1, 2, 3]) == 6
    assert checkio([4, 5, 6]) == 15
    assert checkio([10, 20, 30]) == 60
    print('Done!!!')