N = int(input())

dp = [[0, 0, 0] for _ in range(N + 1)]
dp[1] = list(map(int, input().split()))

for i in range(2, N + 1):
    r, g, b = map(int, input().split())
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b

print(min(dp[N]))
