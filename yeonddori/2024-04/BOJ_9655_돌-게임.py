N = int(input())
dp = [False] * (N + 1)
dp[1] = True
if N > 2:
    dp[3] = True

for i in range(4, N + 1):
    if not dp[i - 1] or not dp[i - 3]:
        dp[i] = True

print('SK' if dp[N] else 'CY')
