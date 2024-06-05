n = int(input())
s = input()
num = 0
total = 0

for i in s:
    if i.isdigit():
        num = num * 10 + int(i)
    else:
        total += num
        num = 0

total += num
print(total)
