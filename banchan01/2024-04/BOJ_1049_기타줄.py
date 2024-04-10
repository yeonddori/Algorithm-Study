n, m = map(int, input().split())

brand = []
for _ in range(m):
    brand.append(list(map(int,input().split())))

set_sort = sorted(brand, key = lambda x:x[0], reverse = False)
each_sort = sorted(brand, key = lambda x:x[1], reverse = False)

set_ddabong = set_sort[0][0]
each_ddabong = each_sort[0][1]

result = 0
if (each_ddabong * 6 < set_ddabong):
    result = n*each_ddabong
    print(result)
else:
    result += (n//6) * set_ddabong
    if (n%6)*each_ddabong > set_ddabong:
        result += set_ddabong
    else:
        result += (n%6)*each_ddabong

    print(result)