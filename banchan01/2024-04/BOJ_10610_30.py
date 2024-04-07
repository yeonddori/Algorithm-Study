n = int(input())

lst = list(map(int,str(n)))
s_lst = sorted(lst,reverse = True)

if (s_lst[-1] != 0 or sum(s_lst) % 3 != 0):
    print(-1)
else:
    result = int(''.join(map(str,s_lst)))
    print(result)