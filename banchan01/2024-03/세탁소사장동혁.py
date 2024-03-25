T = int(input())
lst = []

for _ in range(T):
    received = int(input())
    Q = 25
    D = 10
    N = 5
    P = 1
    result = []

    a = int(received // Q)
    result.append(a)
    received -= Q * a

    b = int(received // D)
    result.append(b)
    received -= D * (b)

    c = int(received // N)
    result.append(c)
    received -= N * (c)

    d = int(received // P)
    result.append(d)
    received -= D * (d)

    if (received <= 0):
        for i in result:
            print(i, end=' ')

    print('')