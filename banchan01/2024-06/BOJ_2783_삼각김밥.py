x, y = map(int, input().split())
lst = [x/y]
for _ in range(int(input())):
    x, y = map(int, input().split())
    lst.append(x/y)
print("%.2f" % (min(lst)*1000))