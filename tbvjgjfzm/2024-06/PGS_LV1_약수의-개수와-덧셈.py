def solution(left, right):
    answer = 0
    dirtn = 0
    for i in range(left, right+1, 1):
        dirtn = 0
        for j in range(1, i+1, 1):
            if i % j == 0:
                dirtn +=1
        if dirtn % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer