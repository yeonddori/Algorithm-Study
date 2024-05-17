M = int(input())

position = [0,1,2,3]
for _ in range(M):
    a, b = map(int, input().split())
    position[a], position[b] = position[b], position[a]
print(position.index(1))