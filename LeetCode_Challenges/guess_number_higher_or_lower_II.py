'https://leetcode.com/problems/guess-number-higher-or-lower-ii/'

'''
We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
'''
import sys
from functools import lru_cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        l = 1
        r = n
        money = 0
        
        while l <= r:
            
            mid = l + (r-l) // 2
            
            if mid < num:
                r = mid - 1
                money = money + mid
            elif mid > num:
                l = mid + 1   
                money = money + mid             
            else:
                return money
            
        return money
    
    def getMoneyAmount_OK(self, n: int) -> int:
        # https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/1406675/Python-oror-DP-oror-AC-in-Python-oror-TLE-in-C%2B%2B
        
        ans=-sys.maxsize
        if n in (1,2):
            return n-1
        @lru_cache(None)
        def dp(l,h):
            if l>=h:
                return 0
            ans=sys.maxsize
            for k in range(l,h+1):
                a=dp(l,k-1)+k
                b=dp(k+1,h)+k
                ans=min(ans,max(a,b))
            return ans
        return dp(1,n)
    
n = 10
num = 2 # the number for guessing
 
my_obj = Solution()
pick = my_obj.getMoneyAmount_OK(n)
print(pick)