def solution(n):
    answer = []
    n = str(n)
    for i in range(0, len(n)):
        answer.append(int(n[i]))
    return list(reversed(answer))