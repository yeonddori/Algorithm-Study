def solution(d, budget):
    sort_d = sorted(d)
    result = 0
    for i in range(0, len(sort_d), 1):
        result += sort_d[i]
        if result > budget:
            answer = i
            break
        elif result == budget:
            answer = i + 1
            break
        answer = i + 1 
    ANSWER = answer 
    return ANSWER