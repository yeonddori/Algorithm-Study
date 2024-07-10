N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = [(0, 0)]

while queue:
    x, y = queue.pop(0)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))

print(maze[N-1][M-1])
