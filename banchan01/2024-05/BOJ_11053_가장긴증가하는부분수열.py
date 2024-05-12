n = int(input())
lst = list(map(int, input().split()))
# 1. dp 정의를 해야함. dp[i] -> 0 ~ i-1 까지 증가하는 수열의 길이
# ex) dp[4] 면 lst[0] ~ lst[3]까지 중에서 증가하는 수열의 길이
# 너무 어렵닭..

dp = [1] * n

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))