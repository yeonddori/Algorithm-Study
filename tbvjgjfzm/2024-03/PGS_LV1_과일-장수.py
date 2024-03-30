def solution(k, m, score):
    s_len = len(score)
    score.sort(reverse = True)
    count = s_len // m
    i = 1
    answer = 0
    while i <= count:
        answer = answer + score[i * m - 1] * m
        i += 1
    return answer