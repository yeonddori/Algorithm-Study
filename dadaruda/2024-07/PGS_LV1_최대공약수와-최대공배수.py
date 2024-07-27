def solution(n, m):
    answer = []
    big = 0
    small = 0
    if n >=m:
        big = n
        small = m
    else:
        big = m
        small = n
    for i in range(small+1, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    for j in range(1,1000):
        if j* big % small == 0:
            answer.append(j*big)
            break
        
    return answer