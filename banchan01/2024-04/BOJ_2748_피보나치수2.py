def fibo(n,memo = {}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n
    else:
        memo[n] = fibo(n-1,memo) + fibo(n-2,memo)
        return memo[n]

def main():
    n = int(input())
    result = fibo(n)
    print(result)

main()