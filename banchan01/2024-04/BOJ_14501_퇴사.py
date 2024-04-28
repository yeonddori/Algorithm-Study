n = int(input())

lst = []

# lst ĭ �ϳ� �÷��ֱ�
lst.append([0,0])

for _ in range(n):
    lst.append(list(map(int,input().split())))

dp = [0] * (n+2)
# �������� �Ի��ߴ�.
# dp[i] �� i ��°���� ���Ҷ�, ���� ���� �� �ִ� �ִ�
# ex) n == 7 �϶�, �������� �����ϴϱ�, dp[7] �� 7�ϱ��� ���� ��.. but ��ǻ� ù�� ���Ѱ���.
# dp[6] �� 6�ϱ��� ���Ѱ�.. but ��ǻ� ��Ʋ ���Ѱ���.
# dp[6] ���Ҷ�, (6���� ���ؼ� ������ + �� �� ������ ���� dp[]�� ����ִ� ��) vs dp[7] ��

for i in range(n,0,-1):
    if ( lst[i][0] + i <= n+1 ):
        dp[i] = max(lst[i][1] + dp[i+lst[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(max(dp))