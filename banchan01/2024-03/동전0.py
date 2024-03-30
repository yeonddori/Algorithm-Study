n,k = map(int,input().split())

money = []
for _ in range(n):
    money.append(int(input()))

# 내림차순 정렬
S_money = sorted(money, reverse=True)

result = 0

for i in range(n):
    if(k >= S_money[i]):
        result += (k // S_money[i])
        k = k % S_money[i]
    if(k==0):
        break

print(result)