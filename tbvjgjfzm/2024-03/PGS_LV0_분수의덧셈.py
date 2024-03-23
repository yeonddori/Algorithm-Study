def solution(numer1, denom1, numer2, denom2):
    answer1 = 0
    answer2 = 0
    if (denom1 > denom2):
        if ((denom1 % denom2) == 0):
            answer1 = numer1 + denom1 // denom2 * numer2
            answer2 = denom1
        else : 
            answer1 = numer1 * denom2 + numer2 * denom1
            answer2 = denom1 * denom2
    elif(denom1 < denom2):
        if ((denom1 % denom2) == 0):
            answer1 = numer2 + denom2 // denom1 * numer1
            answer2 = denom2
        else : 
            answer1 = numer1 * denom2 + numer2 * denom1
            answer2 = denom1 * denom2
    elif(denom1 == denom2):
        answer1 = numer1 + numer2
        answer2 = denom1
    answer = [answer1, answer2]
    # 기약분수로 만들어야됨.
    answer3 = min(answer1, answer2) 
    for i in range(answer3, 1, -1): 
        if (((answer1 % i) == 0) and ((answer2 % i) == 0)): # i 자리에 answer3 넣음.
            answer = [answer1 // i, answer2 // i]
            break
    return answer