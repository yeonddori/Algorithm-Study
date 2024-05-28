def solution(k, score):
    answer = []
    spotlight = []
    result = []
    for i in range(0, len(score), 1):
        spotlight.append(score[i])
        if len(spotlight) <= k:
            spotlight = sorted(spotlight)
            result.append(min(spotlight))
        else:
            spotlight = sorted(spotlight)
            spotlight.remove(spotlight[0])
            result.append(min(spotlight))            
            
    return result