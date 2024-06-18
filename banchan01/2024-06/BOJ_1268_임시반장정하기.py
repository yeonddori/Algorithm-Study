n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))

result = [0]*n

for i in range(n):
    standard = [x for x in lst[i]]
    for j in range(n):
        for k in range(5):
            if standard[k] == lst[j][k]:
                result[i] += 1
                break

ans = 1
maximum = result[0]
for i in range(n):
    if result[i] > maximum:
        maximum = result[i]
        ans = i+1

print(ans)