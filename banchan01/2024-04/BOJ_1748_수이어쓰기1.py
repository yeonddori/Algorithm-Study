n = input()
# �ڸ���
length = len(n)
# ��� ����
result = 0
# �־��� ���� �ڸ���-1 �� �ڸ��� ��� ���ϱ�
for i in range(1,length):
    mini_len = pow(10,i) - pow(10,i-1)
    result += mini_len * i

result += (int(n) - pow(10,length-1) + 1) * length

print(result)