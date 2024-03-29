result = [0,0,0]
lst = []

def main():
    global result
    n = int(input())
    # 2차원 리스트 입력받기
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    Cut(n,0,0)
    print(result[-1])
    print(result[0])
    print(result[1])


def Diff(num,f,s):
    for i in range(f,f+num):
        for j in range(s,s+num):
            if (lst[f][s] != lst[i][j]):
                return True
    return False

def Cut(num,f,s):
    global result
    if (not Diff(num,f,s)):
        result[lst[f][s]] += 1
    else:
        for i in range(0,3):
            for j in range(0,3):
                Cut((num//3), f + (num//3)*i, s + (num//3)*j)

main()