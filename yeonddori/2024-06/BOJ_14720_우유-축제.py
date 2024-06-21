N = int(input())
milk = list(map(int, input().split()))
cnt = 0

for i in milk:
    if i == cnt % 3:
        cnt += 1

print(cnt)
