def solution(players, callings):
    answer = players[:]
    indexes = {player: i for i, player in enumerate(players)}

    for calling in callings:
        index = indexes[calling]
        answer[index], answer[index - 1] = answer[index - 1], answer[index]
        indexes[calling], indexes[answer[index]] = index - 1, index

    return answer
