n,m = map(int,input().split())
situation = []
cnt = 0
for _ in range(n):
    situation.append(list(input()))

for row in situation:
    if 'X' not in row:
        cnt += 1

n_cnt = 0
for i in range(m):
    flag = False
    for j in range(n):
        if situation[j][i] == 'X':
            flag = True
            break
    if flag == False:
        n_cnt += 1
print(max(cnt,n_cnt))