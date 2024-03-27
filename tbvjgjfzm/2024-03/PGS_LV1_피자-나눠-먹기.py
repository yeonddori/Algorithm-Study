def solution(n):
    if ((n >= 1) and (n<= 100)):
        if (n % 6) == 0:
            answer = (n // 6)
        else:
            for i in range(1, 100):
                if ((i * 6) % n) == 0:
                    break
            answer = i
    return answer