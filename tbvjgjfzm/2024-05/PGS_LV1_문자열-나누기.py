def solution(s):
    answer = 0
    count = 1
    ccount = 0
    i = 0
    while i < len(s):
        count = 1
        ccount = 0
        print(answer)
        print(s[i])
        print(100 + i)
        if i != len(s) - 1 and s[i] != s[i+1]:
            answer += 1
            i = i + 2
        elif i == len(s) - 1: # 제일 마지막 하나만 남았을 때
            answer += 1
            break
        elif i != len(s) - 1 and s[i] == s[i+1]:
            for j in range(i+1, len(s), 1):
                if s[i] == s[j] and count != ccount: # 첫번째랑 똑같은 요소 찾기
                    count += 1
                    if count != ccount and j == len(s) - 1: # 안 똑같은데 마지막일 때
                        answer += 1
                        i = i + j + 1
                        break
                elif s[i] != s[j] and count != ccount: # 첫번째랑 안똑같은 요소
                    ccount += 1
                    if count != ccount and j == len(s) - 1: # 안 똑같은데 마지막일 때
                        answer += 1
                        i = i + j + 1
                        break
                    elif count == ccount and j == len(s) - 1: # 없으면 "aabacc"인 경우 에러.
                        answer += 1
                        i = i + j + 1
                        break
                elif count == ccount:
                    answer += 1
                    i = j 
                    break
    return answer


