'https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-92/problems/'

'''
An array is nice, if arr[i] = i, for each index i.
'''

# Not clear why is NOT OK

class Solution:
    def niceSubarray(self, arr):
        answer = [item for idx, item in enumerate(arr) if idx == item]
        
        print(answer)
        return answer
        

if __name__ == '__main__':
    my_object = Solution()
    
    assert my_object.niceSubarray([2,1,2,3,1,2,2]) == [1, 2, 3]
    assert my_object.niceSubarray([3, 5, 2, 6]) == [2]

