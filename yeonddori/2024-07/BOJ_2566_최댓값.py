arr = [[0] * 9 for _ in range(9)]
for i in range(9):
    arr[i] = list(map(int, input().split()))

max_val = max(map(max, arr))
for i in range(9):
    for j in range(9):
        if arr[i][j] == max_val:
            print(max_val)
            print(i+1, j+1)
            break
    else:
        continue
    break
