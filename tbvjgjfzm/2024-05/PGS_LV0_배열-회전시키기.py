def solution(numbers, direction):
    answer = []
    if direction == "right":
        last = [numbers[len(numbers)-1]]
        answer = last + numbers[0:len(numbers)-1]
    else:
        first = [numbers[0]]
        answer = numbers[1:len(numbers)] + first
    return answer