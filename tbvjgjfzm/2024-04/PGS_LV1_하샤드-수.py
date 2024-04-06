def solution(x):
    num = list(map(int,str(x)))
    sum_x = sum(num)
    answer = True
    if x % sum_x == 0:
        answer = True
    else:
        answer = False
    
    return answer