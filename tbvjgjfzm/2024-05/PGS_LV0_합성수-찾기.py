def solution(n):
    answer = 0
    result = 0
    for i in range(1, n+ 1, 1):
        print(i)
        for j in range(1, i + 1, 1):
            if i % j == 0:
                result += 1
        if result >= 3:
            answer += 1
            result = 0
        else:
            result = 0
    return answer