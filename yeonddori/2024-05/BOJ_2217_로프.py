N = int(input())
weight = [int(input()) for _ in range(N)]
weight.sort(reverse=True)

max_weight = 0
for i in range(N):
    max_weight = max(max_weight, weight[i] * (i + 1))

print(max_weight)
