def solution(sizes):
    big = []
    small = []
    answer = 0
    for i in range(0, len(sizes), 1):
        big.append(max(sizes[i]))
        small.append(min(sizes[i]))
    answer = max(big) * max(small)
    return answer