import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sums = [0]

for i in range(N):
    sums.append(sums[i] + nums[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sums[j] - sums[i - 1])
