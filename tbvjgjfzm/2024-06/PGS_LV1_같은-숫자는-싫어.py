def solution(arr):
    answer = []
    arr.append(11)
    for i in range(0, len(arr)-1, 1):
        if arr[i] == arr[i+1]:
            pass
        else:
            answer.append(arr[i])
    return answer