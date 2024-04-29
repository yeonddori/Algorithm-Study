n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j, num in enumerate(map(int, input().split()), 1):
        dp[i][j] = num + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n]))
