n = int(input())

lst = list(map(int,input().split()))
std = lst[0]

down = [0]*(n+1)
up = [0]*(n+1)

down[0] = 1
up[0] = 1

for i in range(1,n):

    if std < lst[i]:
        std = lst[i]
        up[i] += (1 + up[i-1])
        down[i] += 1

    elif std > lst[i]:
        std = lst[i]
        down[i] += (1 + down[i-1])
        up[i] += 1

    elif std == lst[i]:
        std = lst[i]
        up[i] += (1 + up[i-1])
        down[i] += (1 + down[i-1])

u_max = max(up)
d_max = max(down)

print(max(u_max,d_max))