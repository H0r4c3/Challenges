'https://www.hackerrank.com/challenges/alternating-characters/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign'

'''
You are given a string containing characters  and  only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.
'''

def alternatingCharacters(s):
    # Write your code here
    l = s.strip()
    count = 0
    for i in range(len(l)-1):
        if l[i] == l [i+1]:
            count += 1
            i += 1
        else:
            i += 1
    return count

s = 'AABAAB'
count = alternatingCharacters(s)
print(count)


# for answer on site
# if __name__ == '__main__':
#     T = int(input().strip()) # nr. of testcases

#     for _ in range(T):
#         s = input()

#         result = alternatingCharacters(s)
