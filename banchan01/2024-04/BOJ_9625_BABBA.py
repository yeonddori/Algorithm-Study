def fire(k):
    if k==0:
        return 0
    if k==1 or k==2:
        return 1
    lst = [0] * (k+1)
    lst[1] = 1
    lst[2] = 1
    for i in range(3,k+1):
        lst[i] = lst[i-1] + lst[i-2]

    return lst[k]

def main():
    k = int(input())
    A_cnt = fire(k-1)
    B_cnt = fire(k)
    print(A_cnt, B_cnt)

main()