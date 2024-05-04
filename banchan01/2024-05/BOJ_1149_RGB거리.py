N = int(input())

lst = []
# 순서대로 R,G,B 입력받기
for _ in range(N):
    lst.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N + 1)]

dp[1][0] = lst[0][0]
dp[1][1] = lst[0][1]
dp[1][2] = lst[0][2]

for i in range(2, N + 1):
    dp[i][0] = min(dp[i - 1][1] + lst[i - 1][0], dp[i - 1][2] + lst[i - 1][0])
    dp[i][1] = min(dp[i - 1][0] + lst[i - 1][1], dp[i - 1][2] + lst[i - 1][1])
    dp[i][2] = min(dp[i - 1][0] + lst[i - 1][2], dp[i - 1][1] + lst[i - 1][2])

print(min(dp[N][0],dp[N][1],dp[N][2]))
