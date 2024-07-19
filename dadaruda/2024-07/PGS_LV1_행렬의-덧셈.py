def solution(arr1, arr2):
    answer1 = []
    answer2 = []
    for i in range(0, len(arr1), 1):
        for j in range(0, len(arr1[i])):
            answer1.append(arr1[i][j] + arr2[i][j])
        answer2.append(answer1)
        answer1 = []
    return answer2