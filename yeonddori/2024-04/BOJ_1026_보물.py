N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

S = 0
for i in range(N):
    S += A[i] * B.pop(B.index(max(B)))

print(S)
