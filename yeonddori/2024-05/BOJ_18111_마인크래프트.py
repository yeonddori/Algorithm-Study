import sys

N, M, B = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_time = float('inf')
height = 0

for i in range(257):
    block_added = 0
    block_removed = 0
    for j in range(N):
        for k in range(M):
            if land[j][k] < i:
                block_added += i - land[j][k]
            else:
                block_removed += land[j][k] - i

    if block_added > block_removed + B:
        continue

    time = block_added + block_removed * 2
    if time <= min_time:
        min_time = time
        height = i

print(min_time, height)
