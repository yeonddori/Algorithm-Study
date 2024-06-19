t = int(input())

for _ in range(t):
    cnt = 0
    input()
    r,c = map(int,input().split())
    lst = [list(input()) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if lst[i][j] == chr(111):
                if j != 0 and j != c-1 and lst[i][j-1] == chr(62) and lst[i][j+1] == chr(60):
                    cnt += 1
                elif i != 0 and i != r-1 and lst[i-1][j] == chr(118) and lst[i+1][j] == chr(94):
                    cnt += 1
    print(cnt)