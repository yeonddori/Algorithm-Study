import math
n = int(input())

dp = [0]*(n+1)
dp[1] = 1

# �������� 1�� �� ó�����ֱ�
for i in range(2,n+1):
    if math.sqrt(i).is_integer():
        dp[i] = 1

for i in range(2,n+1):
    val = 1000000
    if dp[i] != 1:
        j = 1
        while j*j <= i:
            val = min(val, 1 + dp[i-j*j])
            j += 1
        dp[i] = val

print(dp[n])