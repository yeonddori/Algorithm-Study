T = int(input())

# dp는 점화식을 찾아야함..
# 점화식 찾을때, 항상 기준을 두고 순차적으로 접근해야함
# dp 정해인 존잘임
for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
        continue
    elif n == 2:
        print(2)
        continue
    elif n == 3:
        print(4)
        continue

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
