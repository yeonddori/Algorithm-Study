N = int(input())

l = list(map(int,input().split()))
J = list(map(int,input().split()))
l , J = [0] + l, [0] + J

dp = [[0]*101 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,101):
        if l[i] <= j:
            dp[i][j] = max( dp[i-1][j] , dp[ i-1 ][ j - l[i] ] + J[i] )
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])

