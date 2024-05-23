n = int(input())
lst = list(map(int,str(n)))

r_cnt = [0]*10
c_cnt = [0]*10
for i in range(len(lst)):
    for j in range(len(r_cnt)):
        if lst[i] == j:
            r_cnt[j] += 1
            c_cnt[j] += 1


if (r_cnt[6] + r_cnt[9]) %2 ==0:
    c_cnt[6] = (r_cnt[6] + r_cnt[9]) // 2
    c_cnt[9] = (r_cnt[6] + r_cnt[9]) // 2
else:
    c_cnt[6] = ((r_cnt[6] + r_cnt[9]) // 2) +1
    c_cnt[9] = ((r_cnt[6] + r_cnt[9]) // 2) +1

print(max(c_cnt))