def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 if graph[i][j] == 1 else 0 for j in range(m)] for i in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j)
            break

bfs(start[0], start[1])

for row in visited:
    for col in row:
        print(col, end=' ')
    print()
