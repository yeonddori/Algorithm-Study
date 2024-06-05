def solution(array, n):
    x = len(array)
    i = 0
    answer = 0
    while(i<x):
        if(array[i] == n):
            answer = answer + 1
        i = i + 1
    return answer