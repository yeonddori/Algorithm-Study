n = int(input())

result = 0

# 5�� ������������ ��!!!!, �ƴϸ� 2�� �ϳ��� ���ֱ�
while(n != 0):
    if (n == 1):
        result = -1
        break
    if(n%5 == 0):
        result += n//5
        break
    else:
        n -= 2
        result += 1

print(result)