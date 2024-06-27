N = int(input())
dp = [0] * (N + 1)
dp[1] = 'CY'
dp[2] = 'SK'

for i in range(3, N + 1):
    if dp[i - 1] == 'SK' or dp[i - 3] == 'SK':
        dp[i] = 'CY'
    else:
        dp[i] = 'SK'

print(dp[N])
