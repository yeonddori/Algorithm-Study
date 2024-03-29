def dfs(cnt, start):
    if cnt == M:
        print(*result)
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            result.append(i + 1)
            dfs(cnt + 1, i + 1)
            visited[i] = False
            result.pop()

N, M = map(int, input().split())
visited = [False] * N
result = []

dfs(0, 0)
