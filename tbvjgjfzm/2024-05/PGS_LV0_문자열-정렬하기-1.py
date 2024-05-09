def solution(my_string):
    result = []
    answer = []
    number = ["1","2","3","4","5","6","7","8","9","0"]
    
    for i in range(0, len(my_string), 1):
        for j in range(0, len(number), 1):
            if my_string[i] == number[j]: 
                answer.append(my_string[i])
    answer = list(map(int, answer))
    result = sorted(answer)
    return result