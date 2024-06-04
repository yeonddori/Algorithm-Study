def solution(array, commands):
    answer = []
    for i in range(0, len(commands), 1):
        n_array = array[commands[i][0] - 1 : commands[i][1]]
        n_array = sorted(n_array)
        answer.append(n_array[commands[i][2]-1])
    
    return answer