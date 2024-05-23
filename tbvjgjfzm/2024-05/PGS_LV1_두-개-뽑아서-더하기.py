def solution(numbers):
    answer = []
    for i in range(0, len(numbers), 1):
        for j in range(i+1, len(numbers), 1):
            answer.append(numbers[i] + numbers[j])
    set_answer = set(answer)
    ANSWER = list(set_answer)
    result = sorted(ANSWER)
    # print(ANSWER)
    return result