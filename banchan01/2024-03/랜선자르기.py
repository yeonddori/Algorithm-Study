k, n = map(int, input().split())
lst = []

for _ in range(k):
    lst.append(int(input()))

# �� ����, ������ �� ����
left = 1
right = max(lst)

# �ʱ� mid �� ����
mid = (left+right)//2

# ���� n ����
semi_n = 0

while(left<=right):
    semi_n = 0
    mid = (left + right) // 2

    for i in lst:
        semi_n += i//mid

    if (semi_n < n):
        right = mid-1

    elif (semi_n >= n):
        left = mid + 1

print(right)