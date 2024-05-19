N = int(input())
MOD = 1000000000

# dp ���� -> dp[i][j] �� ���� == i�̰� �� ���ڸ� ���� j �϶�, ��ܼ� ����
# �� '���ڸ�' ���ڸ� j �� �ع����� j==0�� ��츦 ���� ��쿡 ��������� ����.. ( ��~~~~~�� 0�̴ϱ� )
# ex) dp[2][0] == 0 ��. But, dp[3][1] = dp[2][0] + dp[2][2] �ε�,  101 �� ���Ե��� ����.
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