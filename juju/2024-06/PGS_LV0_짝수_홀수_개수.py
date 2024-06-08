def solution(num_list):
    x = 0
    y = 0
    for i in num_list:
        if i % 2 == 0:
            x += 1
        elif i % 2 != 0:
            y += 1
    answer = [x, y]
    return answer