n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
dp[1] = wines[0]
if n > 1:
    dp[2] = wines[0] + wines[1]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + wines[i - 1],
                dp[i - 3] + wines[i - 2] + wines[i - 1])

print(max(dp))
