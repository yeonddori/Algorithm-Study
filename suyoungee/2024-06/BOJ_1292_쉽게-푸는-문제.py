start, end = map(int, input().split())

nums = []

for i in range(end) :
    for j in range(i+1) :
        nums.append(i+1)

s = 0
while start <= end :
    s += nums[start-1]
    start += 1

print(s)