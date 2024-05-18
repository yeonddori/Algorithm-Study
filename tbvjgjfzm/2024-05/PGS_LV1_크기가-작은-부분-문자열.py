def solution(t, p):
    answer = 0
    tstring = ""
    length = len(t) - len(p) + 1
    for i in range(0, length, 1):
        a = i
        for j in range(0, len(p), 1):
            tstring += t[a]
            a += 1
        print(tstring)
        if int(tstring) <= int(p):
            answer += 1
        tstring = ""
    return answer