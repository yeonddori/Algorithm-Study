n, k = map(int,input().split())
weight = []
value = []

weight.append(0)
value.append(0)
for _ in range(n):
    a,b = map(int,input().split())
    weight.append(a)
    value.append(b)

# dp[i][j] -> 배낭 최대무게가 j인 상황에서, i번째 물건까지 판단했을때, 최대 가치
dp = [[0]*(k+1) for _ in range(n+1)]

# 첫번째 ~ n번째 물건까지 검사하기..
for i in range(1,n+1):
    # 가방 최대무게 j 일때..
    for j in range(1,k+1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j], value[i] + dp[i-1][j-weight[i]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])