N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

for i in range(1, N + 1):
    if i + T[i] - 1 <= N:
        dp[i + T[i] - 1] = max(dp[i + T[i] - 1], dp[i - 1] + P[i])
    dp[i] = max(dp[i], dp[i - 1])

print(max(dp))
