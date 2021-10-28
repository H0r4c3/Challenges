'https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/bubble-sort-15-8064c987/'



def bubble_sort(s):
    counter = 0
    my_list = list(map(int, s.split()))
    N = len(my_list)
    swapped = True
    while swapped != False:
        swapped = False
        counter += 1
        for i in range(N-1):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                swapped = True
    
    return counter

s = '1 3 2 5 4'
result = bubble_sort(s)
print(result)