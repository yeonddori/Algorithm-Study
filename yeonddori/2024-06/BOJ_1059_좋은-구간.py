L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())

if n in S:
    print(0)
    exit()

left, right = 0, 1001
for num in S:
    if num < n:
        left = num
    elif num > n:
        right = num
        break

count = 0
for A in range(left + 1, n + 1):
    for B in range(n, right):
        if A < B:
            count += 1

print(count)
