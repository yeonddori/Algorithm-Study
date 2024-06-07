n = int(input())

mod = 15746

# dp[i] -> 길이 i 인 모든 2진수열 개수
dp = [0]*(n+1)

dp[1] = 1
if (n>=2):
    dp[2] =2

for i in range(3,n+1):
    dp[i] = dp[i-1]%mod + dp[i-2]%mod

print(dp[n]%mod)