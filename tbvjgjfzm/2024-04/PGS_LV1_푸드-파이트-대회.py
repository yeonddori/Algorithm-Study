def solution(food):
    answer = []
    for i in range(0, len(food), 1):
        if int(food[i]) > 1:
            eat = int(food[i]) // 2
            for j in range(0, eat, 1):
                answer.append(i)
    rev = list(reversed(answer))
    answer.append(0)
    answer.extend(rev)
    result = ''.join(map(str,answer))
    return result