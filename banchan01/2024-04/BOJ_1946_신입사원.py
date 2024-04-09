T = int(input())

for _ in range(T):
    cnt = 0
    n = int(input())
    score = []
    # 점수 입력 받기
    for _ in range(n):
        score.append(list(map(int,input().split())))


    S_score = sorted(score,key = lambda x:x[0], reverse = False)
    Max = S_score[0][1]

    for i in range(len(S_score)):
        if(S_score[i][1] <= Max):
            cnt += 1
            Max = S_score[i][1]

    print(cnt)