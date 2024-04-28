n = int(input())

lst = []

# lst 칸 하나 늘려주기
lst.append([0,0])

for _ in range(n):
    lst.append(list(map(int,input().split())))

dp = [0] * (n+2)
# 역순으로 게산했다.
# dp[i] 는 i 번째까지 일할때, 갖고 있을 수 있는 최댓값
# ex) n == 7 일때, 역순으로 진행하니깐, dp[7] 은 7일까지 일한 거.. but 사실상 첫날 일한거임.
# dp[6] 은 6일까지 일한거.. but 사실상 이틀 일한거임.
# dp[6] 정할때, (6일차 일해서 받을돈 + 일 다 끝나고 다음 dp[]에 들어있는 돈) vs dp[7] 비교

for i in range(n,0,-1):
    if ( lst[i][0] + i <= n+1 ):
        dp[i] = max(lst[i][1] + dp[i+lst[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(max(dp))