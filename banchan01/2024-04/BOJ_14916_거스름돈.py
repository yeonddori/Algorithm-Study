n = int(input())

result = 0

# 5로 나눠떨어지면 끗!!!!, 아니면 2로 하나씩 빼주기
while(n != 0):
    if (n == 1):
        result = -1
        break
    if(n%5 == 0):
        result += n//5
        break
    else:
        n -= 2
        result += 1

print(result)