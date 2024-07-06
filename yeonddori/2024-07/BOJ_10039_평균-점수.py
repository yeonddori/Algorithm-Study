avg = 0

for _ in range(5):
    score = int(input())
    avg += score if score >= 40 else 40

print(avg // 5)
