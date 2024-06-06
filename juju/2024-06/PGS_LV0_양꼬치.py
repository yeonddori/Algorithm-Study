def solution(n, k):
    i = n // 10
    j = k - i
    answer = (n * 12000) + (j * 2000)
    return answer