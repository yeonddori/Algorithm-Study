def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes), 1):
        if signs[i] == False:
            answer -= absolutes[i]
        elif signs[i] == True:
            answer += absolutes[i]
        print(answer)
    return answer