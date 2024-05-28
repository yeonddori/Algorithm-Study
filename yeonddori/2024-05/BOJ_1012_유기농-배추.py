from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if field[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if field[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)
