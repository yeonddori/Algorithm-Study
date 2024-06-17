while True:
    B, N = map(int, input().split())
    if B == 0 and N == 0:
        break

    answer = 0
    for i in range(1, 1000000):
        if i ** N <= B:
            answer = i
        else:
            break

    if B - answer ** N <= (answer + 1) ** N - B:
        print(answer)
    else:
        print(answer + 1)
