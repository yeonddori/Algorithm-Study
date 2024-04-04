def solution(emergency):
    new = sorted(emergency)
    answer = []
    for i in range(0, len(emergency) , 1):
        for j in range(0, len(new), 1):
            if emergency[i] == new[j]:
                answer.append(len(emergency) - j)
            else:
                pass
    return answer