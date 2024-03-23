N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total < M:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
