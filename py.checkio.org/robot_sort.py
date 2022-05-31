'https://py.checkio.org/en/mission/robot-sort/'

'''
You are given the sizes and initial order of the rods as an array of numbers. 
Indexes are position, values are sizes. You should order this array from the smallest to the largest in size.
'''

def swapsort(array):
    array = list(array)
    result = list()
    while array != sorted(array):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                result.append(str(i) + str(i+1))
    
    return ','.join(result)


# Best Solution: 
# https://py.checkio.org/mission/robot-sort/publications/pokosasa/python-3/first/share/dbcb969f6f2945a40c658d369d93137c/

def swapsort_(array):
    N=len(array)
    array=list(array)
    res=[]
    while True:
        updated=False    
        for i in range(N-1):
            if array[i]<=array[i+1]:
                continue
            array[i],array[i+1]=array[i+1],array[i]
            res.append(str(i)+str(i+1))
            updated=True
        if updated:
            continue
        break
    return ",".join(res)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(f, indata):
        result = f(indata)
        array = list(indata[:])
        la = len(array)
        if not isinstance(result, str):
            print("The result should be a string")
            return False
        actions = result.split(",") if result else []
        for act in actions:
            if len(act) != 2 or not act.isdigit():
                print("The wrong action: {}".format(act))
                return False
            i, j = int(act[0]), int(act[1])
            if i >= la or j >= la:
                print("Index error: {}".format(act))
                return False
            if abs(i - j) != 1:
                print("The wrong action: {}".format(act))
                return False
            array[i], array[j] = array[j], array[i]
        if len(actions) > (la * (la - 1)) // 2:
            print("Too many actions. BOOM!")
            return False
        if array != sorted(indata):
            print("The array is not sorted. BOOM!")
            return False
        return True

    assert check_solution(swapsort, (6, 4, 2)), "Reverse simple"
    assert check_solution(swapsort, (1, 2, 3, 4, 5)), "All right!"
    assert check_solution(swapsort, (1, 2, 3, 5, 3)), "One move"
    print('Done!')