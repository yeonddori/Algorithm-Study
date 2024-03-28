def dfs(cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            dfs(cnt + 1)
            visited[i] = False
            result.pop()

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
visited = [False] * N
result = []

dfs(0)
