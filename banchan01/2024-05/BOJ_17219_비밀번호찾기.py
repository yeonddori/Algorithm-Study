n,m =  map(int,input().split())
info = {}
want = []
for _ in range(n):
    a,b = input().split()
    info[a] = b

for _ in range(m):
    want.append(input())

for ads in want:
    print(info[ads])