import sys

N, M = map(int, sys.stdin.readline().split())
pokemon = {}

for i in range(1, N + 1):
    name = sys.stdin.readline().strip()
    pokemon[name] = i
    pokemon[str(i)] = name

for _ in range(M):
    print(pokemon[sys.stdin.readline().strip()])
