import sys

A, B = map(int, sys.stdin.readline().split())

lst = [1]*100001                           
lst[0], lst[1] = 0, 0                       

for i in range(2, 100001):
    n = 2
    while i*n < 100001:
        lst[i*n] = 0
        n += 1

prime_lst = []                              
for idx, val in enumerate(lst):
    if val == 1:
        prime_lst.append(idx)

result = 0
for num in range(A, B+1):
    temp = num
    temp_lst = []                          
    cnt, n = 0, 0                         

    if lst[temp] == 1:                     
        continue

    while temp > 1:
        if lst[temp]:                    
            cnt += lst[temp]
            temp = 1                     
        else:
            if temp % prime_lst[n]:       
                n += 1                      
            else:                         
                temp_lst.append(temp)      
                temp //= prime_lst[n]
                cnt += 1                 

    for idx, val in enumerate(temp_lst):   
        lst[val] = cnt - idx            

    if lst[cnt] == 1:                      
        result += 1

print(result)