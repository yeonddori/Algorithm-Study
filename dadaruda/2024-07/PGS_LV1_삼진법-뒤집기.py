def solution(n):
    answer = 0
    third = []
    j = 0
    for i in range (1, 100):
        if 3 ** i > n:
            if  3**(i-1)*2 > n:
                third.append(1)
                n -= 3**(i-1)
                j = i-2
                break
            else:
                third.append(2)
                n -= 3**(i-1) * 2
                j = i-2
                break
    for k in range(j, -1, -1):
        if  3**(k)*1 > n:
            third.append(0)
        elif 3**(k)*2 <= n and 3**(k) < n:
            third.append(2)
            n -= 3**(k) * 2
        else:
            third.append(1)
            n -= 3**(k)
    r_third = list(reversed(third))
    print(r_third)
    for t in range(len(third), 0, -1):
        answer += 3 ** (t-1) * r_third[len(third)-t]
        print(answer)
    return answer