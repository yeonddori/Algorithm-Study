T = int(input())
for _ in range(T):
    result = 1
    lst = []
    category = {}
    n = int(input())
    for _ in range(n):
        a,b = input().split()
        lst.append([a,b])
        category[b] = 0
    for a,b in lst:
        category[b] += 1

    for key,val in category.items():
        if val != 1:
            result *= (val+1)
        else:
            result *= 2
    print(result - 1)