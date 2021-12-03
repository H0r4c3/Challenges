

def name_of_method(s, A):
    result = 0

    return result


if __name__ == '__main__':
    T = int(input().strip()) # nr. of testcases

    for _ in range(T):
        s = input() # string
        A = list(map(int, input().split())) # list of integers

        result = name_of_method(s, A)
        
        print(result)