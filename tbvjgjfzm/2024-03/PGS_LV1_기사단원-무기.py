import math
def solution(number, limit, power):
    answer = 0
    status = 0
    for i in range(1, number+1, 1):
        make_sqrt = int(math.sqrt(i))
        for j in range(1, make_sqrt + 1, 1):
            if (i % j) == 0:
                status = status + 1
        if (make_sqrt**2 == i):
            result = status * 2 - 1
        else:result = status * 2
        if (result <= limit):
            result = result
        else:
            result = power
        answer = answer + result
        status = 0
    return answer