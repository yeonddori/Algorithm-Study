n, m, b = map(int,input().split())

lst = []
for _ in range(n):
    lst += list(map(int, input().split()))

time = 0
min_time = 1000000000000000
result = 0

inventory = b
min_height = min(lst)
max_height = max(lst)
sum_height = sum(lst)

for standard in range(min_height,max_height+1):
    inventory = b
    # �κ��丮�� ����ִ� ��� �����ȿ��� �������� �ؾ���.
    if (sum_height + inventory >= standard*n*m):
        time = 0
        for i in range(0, len(lst)):
            # idx���� �������ذ� �� �� -> diff
            diff = lst[i] - standard

            if (diff > 0):
                time += diff*2
                inventory += diff*1

            elif (diff < 0):
                time += abs(diff)*1
                inventory -= abs(diff)*1

        if (time <= min_time and inventory >= 0):
            min_time = time
            result = standard

print(min_time, result)