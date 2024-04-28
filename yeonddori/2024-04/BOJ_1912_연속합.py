n = int(input())
sequence = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1] + sequence[i], sequence[i])

print(max(dp[1:]))
