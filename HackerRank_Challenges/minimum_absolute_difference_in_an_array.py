'https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign'

'''
Given an array of integers, find the minimum absolute difference between any two elements in the array.
'''

def minimumAbsoluteDifference_OK(arr):
    arr.sort()
    result = min(arr[i+1]-arr[i] for i in range(len(arr)-1))
    return result

s = '1 -3 71 68 17'
arr = list(map(int, s.rstrip().split()))

result = minimumAbsoluteDifference_OK(arr)

print(result)