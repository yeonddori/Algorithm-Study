M = int(input())
cups = [1, 0, 0]

for _ in range(M):
    X, Y = map(int, input().split())
    cups[X - 1], cups[Y - 1] = cups[Y - 1], cups[X - 1]

print(cups.index(1) + 1)
