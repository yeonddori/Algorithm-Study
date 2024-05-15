T = int(input())
p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1
p[4] = 2
p[5] = 2

for _ in range(T):
    n = int(input())
    if(n>=1 and n<=5):
        print(p[n])
        continue
    else:
        for i in range(6, n + 1):
            p[i] = p[i - 1] + p[i - 5]
        print(p[n])