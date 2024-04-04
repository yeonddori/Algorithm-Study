N = int(input())
stair = [0]
for _ in range(N):
    stair.append(int(input()))

dp = [0] * (N + 1)
dp[1] = stair[1]

if N > 1:
    dp[2] = stair[1] + stair[2]
for i in range(3, N + 1):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[N])
