T = int(input())

# dp�� ��ȭ���� ã�ƾ���..
# ��ȭ�� ã����, �׻� ������ �ΰ� ���������� �����ؾ���
# dp ������ ������
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
