n = int(input())
num = 0
result = 0
while(n!=0):
    if n<=num:
        num = 0
    result += 1
    num += 1
    n -= num

print(result)