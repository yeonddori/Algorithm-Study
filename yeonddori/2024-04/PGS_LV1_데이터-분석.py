def solution(data, ext, val_ext, sort_by):
    answer = []
    types = ['code', 'date', 'maximum', 'remain']

    for value in data:
        if value[types.index(ext)] < val_ext:
            answer.append(value)

    answer.sort(key=lambda x: x[types.index(sort_by)])

    return answer
