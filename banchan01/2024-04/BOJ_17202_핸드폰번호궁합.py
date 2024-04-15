A = list(map(int,input()))
B = list(map(int,input()))

lst = []
for n1, n2 in zip(A,B):
    lst.append(n1)
    lst.append(n2)

while(len(lst)!=2):
    n_lst = []
    for i in range(len(lst) - 1):
        n_lst.append((lst[i] + lst[i + 1]) % 10)
    lst = n_lst

result = ''.join(map(str,lst))
print(result)