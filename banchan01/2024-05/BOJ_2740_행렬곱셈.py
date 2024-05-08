n, m = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))

m, k = map(int,input().split())
B = []
for _ in range(m):
    B.append(list(map(int,input().split())))

C = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for x in range(m):
            C[i][j] += A[i][x] * B[x][j]

for i in range(n):
    for j in range(k):
        print(C[i][j],end = ' ')
    print()