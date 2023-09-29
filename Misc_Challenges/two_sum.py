'https://www.codingninjas.com/codestudio/problems/two-sum_839653'

'''
you-are-given-an-array-of-integers-arr-of-length-n-and-an-integer-target-your-task-is-to-return-all-pairs-of-elements-such-that-they-add-up-to-target
'''



def twoSum(arr, target, n):
    result = list()
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            print(f'{arr[i]} + {arr[j]}')
            if arr[i] + arr[j] == target:
                result.append((arr[i], arr[j]))
    if result:
        return result
    else:
        return [(-1, -1)]
    
def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))
            
# def printAns(ans):
#     for i in ans:
#         if i[0] < i[1]:
#             print(f'{i[0]} {i[1]}')
#         else:
#             print(f'{i[1]} {i[0]}')

arr = [2, 7, 11, 13]
target = 9
n = 4
result = twoSum(arr, target, n)
print(result)

# Solution using the function printAns()
ans = twoSum(arr, target, n)
printAns(ans)