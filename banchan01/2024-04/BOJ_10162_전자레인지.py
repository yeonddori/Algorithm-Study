T = int(input())
A = 300
B = 60
C = 10

result = []
result.append(T//A)
T %= A
result.append(T//B)
T %= B
result.append(T//C)
T %= C

if (T != 0):
    print(-1)
else:
    for i in result:
        print(i, end = ' ')