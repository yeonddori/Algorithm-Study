import sys

N, M = map(int, sys.stdin.readline().split())
password = {}

for _ in range(N):
    site, pw = sys.stdin.readline().split()
    password[site] = pw

for _ in range(M):
    print(password[sys.stdin.readline().strip()])
