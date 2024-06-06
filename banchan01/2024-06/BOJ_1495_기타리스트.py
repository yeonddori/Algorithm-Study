n, s, m = map(int,input().split())
V = list(map(int,input().split()))
# dp[i][j] -> i번째 곡에서, 가질 수 있는 볼륨 idx == j
dp = [[0]*(m+1) for _ in range(n+2)]
dp[1][s] = 1
result = 0

for i in range(2,n+2):
    update = False

    for j in range(m+1):
        if dp[i-1][j] == 1 and j-V[i-2] >= 0:
            dp[i][j-V[i-2]] = 1
            update = True

        if dp[i-1][j] == 1 and j+V[i-2] <= m:
            dp[i][j+V[i-2]] = 1
            update = True

    if update == False:
        result = -1

result_lst = []
for j in range(m+1):
    if dp[n+1][j] == 1:
        result_lst.append(j)

if result == -1:
    print(result)
else:
    print(max(result_lst))