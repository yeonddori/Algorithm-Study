N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]
leaders = [0] * N

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(5):
            if students[i][k] == students[j][k]:
                leaders[i] += 1
                break

print(leaders.index(max(leaders)) + 1)
