def solution(n, m, section):
    answer = 1
    paint = section[0] + m - 1
    for i in range(1, len(section), 1):
        if paint >= section[i]:
            pass
        else:
            paint = section[i] + m - 1 # paint += m -> 반례 입력값 〉 5, 2, [1, 4, 5]기댓값 〉 2
            answer += 1
    
    return answer