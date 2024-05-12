A, B = input().split()
LA = len(A)
LB = len(B)
result = []

for i in range(LB-LA+1):
    cnt = 0
    for j in range(LA):
        if A[j] != B[i+j]:
            cnt += 1
    result.append(cnt)
print(min(result))