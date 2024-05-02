def solution(numbers, k):
    answer = 0
    i=0
    for j in range (1, k + 1, 1):
        if i < len(numbers):
            answer = numbers[i]
            i += 2
        else:
            answer = numbers[i%len(numbers)]
            i += 2
    return answer