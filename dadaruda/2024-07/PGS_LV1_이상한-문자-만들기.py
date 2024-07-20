def solution(s):
    answer = ''
    l = len(s)
    count = 0
    for i in range(0, l, 1):
        if s[i] != ' ':
            if count % 2 == 0:
                answer += s[i].upper()
                count += 1
            else:
                answer += s[i].lower()
                count += 1
        else:
            answer += s[i]
            count = 0
    return answer