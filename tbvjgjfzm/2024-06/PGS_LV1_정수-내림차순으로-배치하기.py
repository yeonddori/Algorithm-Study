def solution(n):
    answer = 0
    result = []
    k = 1
    i = 10
    while n > 0:
        result.append(n % i // (i//10))
        n = (n - n%i) 
        i *= 10
    result = sorted(result)
    print(result)
    for j in range(0, len(result), 1):
        answer += result[j] * k
        k *= 10
    return answer