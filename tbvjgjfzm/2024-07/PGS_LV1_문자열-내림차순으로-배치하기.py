def solution(s):
    s = list(s)
    s = sorted(s)
    s = list(reversed(s))
    s = ''.join(s)
    answer = s
    return answer