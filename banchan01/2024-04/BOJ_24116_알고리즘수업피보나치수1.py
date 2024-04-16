recur_cnt = 0

def fib(n):
    lst = [0] * (n+1)
    lst[1], lst[2] = 1,1
    for i in range(3,n+1):
        lst[i] = lst[i-1] + lst[i-2]

    return lst[n]


def dy_fib(n):

    if(n==0 or n==1):
        return 1

    lst = [0] * (n+1)
    lst[1] = 1

    for i in range(2,n+1):
        lst[i] = lst[i-1] + lst[i-2]

    return lst[n]

def main():
    n = int(input())
    print(fib(n), n-2)

main()