n = int(input())
lst =[]
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

max_weight = 0

cnt = 1

for i in lst:
    Sum = 0
    Sum += i*cnt
    if(Sum > max_weight):
        max_weight = Sum
    cnt += 1

print(max_weight)