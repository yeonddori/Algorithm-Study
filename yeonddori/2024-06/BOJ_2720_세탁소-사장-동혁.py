T = int(input())

for _ in range(T):
    C = int(input())
    coin = [0, 0, 0, 0]
    coin[0] = C // 25
    C %= 25
    coin[1] = C // 10
    C %= 10
    coin[2] = C // 5
    C %= 5
    coin[3] = C
    print(*coin)
