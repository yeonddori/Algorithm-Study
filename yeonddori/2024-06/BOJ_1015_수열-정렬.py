N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
P = []

for i in range(N):
    P.append(B.index(A[i]))
    B[B.index(A[i])] = -1

print(*P)
