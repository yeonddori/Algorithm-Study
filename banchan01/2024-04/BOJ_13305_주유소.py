city = int(input())

distance = list(map(int,input().split()))
price = list(map(int,input().split()))

standard = price[0]
oil = 0
for i in range(len(price)-1):
    if(standard >= price[i]):
        standard = price[i]
    oil += standard*distance[i]
print(oil)