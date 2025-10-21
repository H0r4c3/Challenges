'''
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. 
If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''


def subset_sum(S, k):
    def backtrack(start, target, current_subset):
        # Base case: if the target is zero, we found a subset
        if target == 0:
            return current_subset
        
        # If the target becomes negative, there's no valid subset
        if target < 0:
            return None

        # Explore subsets starting from the current index
        for i in range(start, len(S)):
            result = backtrack(i + 1, target - S[i], current_subset + [S[i]])
            print(result)
            if result is not None:
                #print(result)
                return result

        return None  # No subset found

    return backtrack(0, k, [])



S = [12, 1, 61, 5, 9, 2]
k = 24

result = subset_sum(S, k)
print(result)