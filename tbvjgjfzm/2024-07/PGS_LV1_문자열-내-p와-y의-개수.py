def solution(s):
    answer = True
    pcount = 0
    ycount = 0
    s = s.upper()
    for i in range(0, len(s), 1):
        if s[i] == "P":
            pcount += 1
        elif s[i] == "Y":
            ycount += 1
    
    if pcount == ycount:
        answer = True
    else:
        answer = False
    return answer