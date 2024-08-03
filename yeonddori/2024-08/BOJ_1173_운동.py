N, m, M, T, R = map(int, input().split())
X = m
time = 0
cnt = 0

while cnt < N:
    if X + T <= M:
        X += T
        cnt += 1
    else:
        X = max(m, X - R)

    time += 1
    if X + T > M and X == m:
        print(-1)
        break
else:
    print(time)
