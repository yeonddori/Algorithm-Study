def solution(n):
    for i in range(1, n+1):
        if i * i == n:
            answer = (i+1)**2
            break
        else:
            answer = -1
    return answer