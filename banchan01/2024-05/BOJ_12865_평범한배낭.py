n, k = map(int,input().split())
weight = []
value = []

weight.append(0)
value.append(0)
for _ in range(n):
    a,b = map(int,input().split())
    weight.append(a)
    value.append(b)

# dp[i][j] -> �賶 �ִ빫�԰� j�� ��Ȳ����, i��° ���Ǳ��� �Ǵ�������, �ִ� ��ġ
dp = [[0]*(k+1) for _ in range(n+1)]

# ù��° ~ n��° ���Ǳ��� �˻��ϱ�..
for i in range(1,n+1):
    # ���� �ִ빫�� j �϶�..
    for j in range(1,k+1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j], value[i] + dp[i-1][j-weight[i]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])