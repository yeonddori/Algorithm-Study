def solution(n):
    answer = 1
    for i in range(1, 12, 1):
        answer = answer * i
        print(answer)
        if n < answer:
            print(i)
            break 
    return i-1