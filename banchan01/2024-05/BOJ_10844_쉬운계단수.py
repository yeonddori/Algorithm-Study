N = int(input())
MOD = 1000000000

# dp 정의 -> dp[i][j] 는 길이 == i이고 젤 뒷자리 숫자 j 일때, 계단수 갯수
# 젤 '앞자리' 숫자를 j 로 해버리면 j==0일 경우를 다음 경우에 사용하지를 못함.. ( 꼐~~~~~속 0이니깐 )
# ex) dp[2][0] == 0 임. But, dp[3][1] = dp[2][0] + dp[2][2] 인데,  101 이 포함되지 못함.
dp = [[0]*10 for _ in range(N+1)]

for j in range(1,10):
    dp[1][j] = 1

for i in range(2,N+1):
    for j in range(0,10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]%MOD
        elif j == 9:
            dp[i][j] = dp[i-1][j - 1]%MOD
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%MOD

result = sum(dp[N])
print(result%MOD)