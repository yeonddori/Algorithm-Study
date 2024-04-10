def dfs(idx, num, visited):
    if idx == k:
        result.add(num)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(idx + 1, num + cards[i], visited)
            visited[i] = False


n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
result = set()

dfs(0, '', [False] * n)
print(len(result))
