def solution(x, n):
    answer = []
    for i in range(1, n + 1, 1):
        answer.append(i* x)
        i += 1
    return answer