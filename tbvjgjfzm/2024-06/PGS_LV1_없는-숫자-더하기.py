def solution(numbers):
    answer = -1
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, len(numbers), 1):
        num.remove(numbers[i])
    print(num)
    answer = sum(num)
    return answer