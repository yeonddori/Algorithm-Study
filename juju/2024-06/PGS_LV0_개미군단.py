def solution(hp):
    j = hp // 5
    b = (hp % 5) // 3
    i = (hp % 5) % 3
    answer = j + b + i
    return answer 