N = int(input())
guests = list(map(int, input().split()))
seats = [False] * 101
cnt = 0

for guest in guests:
    if seats[guest]:
        cnt += 1
    else:
        seats[guest] = True

print(cnt)
