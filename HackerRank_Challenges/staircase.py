'https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_v=zen'

def staircase(n, m):
    if n==1:
        print(m*'#')
    else:
        row = (n-1)*' ' + (m-n+1)*'#'
        print(row)
        staircase(n-1, m)

if __name__ == '__main__':
    print('Enter an integer: ', end='')
    n = int(input().strip())
    m = n

    staircase(n, m)