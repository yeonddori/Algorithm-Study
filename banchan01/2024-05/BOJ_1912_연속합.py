n = int(input())

lst = list(map(int,input().split()))

dp = [0]*(n)

# 음수일때만 포함 시킬지 말지 따지면 안됨.
# 모든 요소에 대해서 판단을 해줘야 dp가 일반화가 됨.
dp[0] = lst[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+lst[i], lst[i])

print(max(dp))