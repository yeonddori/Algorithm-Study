n = int(input())

for _ in range(n):
    m = int(input())
    clothes = {}

    for _ in range(m):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    result = 1

    for c in clothes.values():
        result *= c + 1

    print(result - 1)
