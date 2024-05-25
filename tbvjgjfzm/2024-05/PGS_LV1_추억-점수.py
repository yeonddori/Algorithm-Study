def solution(name, yearning, photo):
    result = 0
    answer = []
    for i in range(0, len(photo), 1):
        for j in range(0, len(photo[i]), 1):
            for k in range(0, len(name), 1):
                if photo[i][j] == name[k]:
                    result += yearning[k]
        answer.append(result)
        result = 0
    return answer