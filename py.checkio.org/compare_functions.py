'https://py.checkio.org/en/mission/comp-funcs/'

'''
Two functions f and g are provided as inputs to checkio . The first function f is the primary function and the second function g is the backup. 
Use your coding skills to return a third function h which returns the same output as f unless f raises an exception or returns None . 
In this case h should return the same output as g . If both f and g raise exceptions or return None , then h should return None .
'''

def checkio(f,g):

    # Replace with your code
    def h(*args,**kwargs):
        return (f(*args,**kwargs),'same')
    return h



# Best Solution: 
# https://py.checkio.org/mission/comp-funcs/publications/veky/python-3/def-def-def/?ordering=most_voted&filtering=all

def checkio(*funcs):
    def result(*args, **kwargs):
        def ignore_exc(k):
            try: return k(*args, **kwargs)
            except Exception: pass
        fr, gr = map(ignore_exc, funcs)
        if fr is gr is None: return None, 'both_error'
        elif fr is None: return gr, 'f_error'
        elif gr is None: return fr, 'g_error'
        else: return fr, 'same' if fr == gr else 'different'
    return result


# Best Solution:
# https://py.checkio.org/mission/comp-funcs/publications/tom-tom/python-3/first/?ordering=most_voted&filtering=all

def checkio(f,g):
    
    def h(*args,**kwargs):
        try:
            f_res = f(*args,**kwargs)
        except:
            f_res = None
        try:
            g_res = g(*args,**kwargs)
        except:
            g_res = None

        if f_res is None:
            return (g_res, 'both_error' if g_res is None else 'f_error')
        else:
            return (f_res, 'g_error' if g_res is None
                            else 'same' if f_res == g_res else 'different')

    return h


if __name__ == '__main__':
       
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    # (x+y)(x-y)/(x-y)
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,3)==(4,'same'), "Function: x+y, first"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,2)==(3,'same'), "Function: x+y, second"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1.01)==(2.01,'different'), "x+y, third"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1)==(2,'g_error'), "x+y, fourth"

    # Remove odds from list               
    f = lambda nums:[x for x in nums if ~x%2]
    def g(nums):
      for i in range(len(nums)):
        if nums[i]%2==1:
          nums.pop(i)
      return nums 
    assert checkio(f,g)([2,4,6,8]) == ([2,4,6,8],'same'), "evens, first"
    assert checkio(f,g)([2,3,4,6,8]) == ([2,4,6,8],'g_error'), "evens, second"         
    
    # Fizz Buzz    
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (6)==('Fizz','same'), "fizz buzz, first"      
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (30)==('Fizz Buzz','same'), "fizz buzz, second"
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (7)==('7','different'), "fizz buzz, third"
                   
    print('Done!!!')