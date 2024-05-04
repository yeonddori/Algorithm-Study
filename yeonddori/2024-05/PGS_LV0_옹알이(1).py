def solution(babbling):
    answer = 0
    pronunciation = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        for j in pronunciation:
            if j in i:
                i = i.replace(j, "-")
        if i.count("-") == len(i):
            answer += 1

    return answer
