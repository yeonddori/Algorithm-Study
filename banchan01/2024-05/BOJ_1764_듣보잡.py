import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = []
for _ in range(n):
    listen.append(input().strip())
see = []
for _ in range(m):
    see.append(input().strip())

listen = set(listen)
see = set(see)
intersection = listen & see

sorted_intersection = sorted(intersection)

print(len(sorted_intersection))
for i in sorted_intersection:
    print(i)
