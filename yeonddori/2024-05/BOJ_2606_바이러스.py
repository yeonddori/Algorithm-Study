def dfs(v):
    global count
    visited[v] = True
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(count - 1)
