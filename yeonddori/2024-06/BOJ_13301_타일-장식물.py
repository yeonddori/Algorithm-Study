N = int(input())
dp = [0, 1, 1]

for i in range(3, N+1):
    dp.append(dp[i-1] + dp[i-2])

print(dp[N]*2 + (dp[N] + dp[N-1])*2)
