
'https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-93/problems/'


# My Solution = Time too long, must be optimized!!!

def maxChocolates(n, m, Arr):
    total_buc = sum(Arr)
    print(f'total_buc = {total_buc}')
    each_student_buc = total_buc / m
    max_buc = int(each_student_buc)
    print(f'max_buc = {max_buc}')
    
    if max_buc == 0:
        return 0
    
    while max_buc > 0: 
        new_arr = list(map(lambda x: int(x/max_buc), Arr))
        print(f'new_arr = {new_arr}')
        total = sum(new_arr)
        print(f'total = {total}')
            
        if total >= m:
            print(f'Result = {max_buc}')
            return max_buc
        else:
            max_buc -= 1

class Solution:
    def maxChocolates(self, n, m, Arr):
        total_buc = sum(Arr)
        each_student_buc = total_buc / m
        max_buc = int(each_student_buc)
        
        if max_buc == 0:
            return 0
        
        while max_buc > 0: 
            new_arr = map(lambda x: int(x/max_buc), Arr)
            total = sum(new_arr)
                
            if total >= m:
                return max_buc
            else:
                max_buc -= 1

my_obj = Solution()

if __name__ == '__main__':
    assert my_obj.maxChocolates(3, 16, [1, 8, 7, 6, 9, 2, 8]) == 2
    assert my_obj.maxChocolates(9, 8, [9, 5, 2, 3, 3, 7, 9, 5, 2]) == 3
    print('Done!!!')