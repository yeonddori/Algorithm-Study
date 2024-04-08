S = list(map(int,input()))

cnt0 = 0
cnt1 = 0

if(S[0] == 1):
    flag = -1000
elif(S[0] == 0):
    flag = 1000

for i in S:
    if(i == 0 and flag == 1000 ):
        cnt0 += 1
        flag = -1000
    elif(i == 1 and flag == -1000):
        cnt1 += 1
        flag = 1000

print(min(cnt0,cnt1))