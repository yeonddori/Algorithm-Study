def factorial(n) -> int:
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

def combination(n,m)-> int:
    son = factorial(n) // factorial(n-m)
    mother =  factorial(m)
    return son // mother

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    result = combination(m,n)
    print(result)