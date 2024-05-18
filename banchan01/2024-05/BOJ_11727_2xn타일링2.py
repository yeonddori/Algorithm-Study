n = int(input())
dp = [0]*(n+1)

dp[1] = 1

if n >= 2:
    dp[2] = 3
# 가로 2칸짜리가 2종류 있으니깐 x2 해주기
for i in range(3,n+1):
    dp[i] = dp[i-1]%10007 + (2*dp[i-2])%10007

print(dp[n]%10007)