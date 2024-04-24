a,b,n = map(int, input().split())

for i in range(n):
    a %= b
    a *= 10
    if i==n-1:
        print(a//b)