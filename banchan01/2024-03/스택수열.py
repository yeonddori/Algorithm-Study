n  = int(input())

# ������������ ���ڳִ� ����Ʈ
stack = []

# ��� ��� ����Ʈ
result = []

first = 1

# �������� �־��� ���� ����Ʈ ����
sequence = []
for _ in range(n):
    sequence.append(int(input()))


for i in sequence:

    if(first <= i):
        while(first <= i):
            stack.append(first)
            result.append('+')
            first += 1

    if (stack[-1] == i):
        stack.pop(-1)
        result.append('-')
    else:
        result = ['NO']
        break

for i in result:
    print(i)