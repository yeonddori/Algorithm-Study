n = int(input())
flag = True

if(len(str(n))==1):
    flag = False

else:
    lst = list(str(n))
    for i in range(1,len(str(n))):
        pre = 1
        back = 1
        for n in lst[:i]:
            pre *= int(n)

        for n in lst[i:]:
            back *= int(n)

        if(pre == back):
            flag = True
            break
        else:
            flag = False

if flag==True:
    print('YES')
else:
    print('NO')