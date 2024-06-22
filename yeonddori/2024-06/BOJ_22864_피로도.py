A, B, C, M = map(int, input().split())
energy = 0
work = 0

for i in range(24):
    if energy + A <= M:
        energy += A
        work += B
    else:
        energy -= C
        if energy < 0:
            energy = 0

print(work)
