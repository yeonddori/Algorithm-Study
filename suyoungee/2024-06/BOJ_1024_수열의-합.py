N, L = map(int, input().split())

result = []
temp = 0

while(1):
    start = int((2*N-L*L+L)*(2*L)**(-1))
    end = start + L -1

    if (start < 0):
        start += abs(start)
        end += abs(start)

    for i in range(start, end+1):
        result.append(i)
        temp += i

    if(temp == N):
        break
    else:
        result = []
        temp = 0
        L += 1
        if (L > 100):
            result.append(-1)
            break

for k in result:
    print(k, end=" ")