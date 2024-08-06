import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0

    for a in range(1, n):
        for b in range(a + 1, n):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                cnt += 1

    print(cnt)
