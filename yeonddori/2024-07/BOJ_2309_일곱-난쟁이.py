height = []

for _ in range(9):
    height.append(int(input()))

height.sort()
total = sum(height)

for i in range(9):
    for j in range(i + 1, 9):
        if total - height[i] - height[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(height[k])
            exit()
