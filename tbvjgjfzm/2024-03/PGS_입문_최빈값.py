from collections import Counter

def solution(array):
    cnt = Counter(array)
    new = dict(cnt)
    just_values = list(new.values())
    just_keys = list(new.keys())
    max_value = max(just_values)
    howmany = 0
    for i in range(0, len(just_values), 1):
        if max_value == just_values[i]:
            howmany = howmany + 1
    if howmany == 1:
        for j in range(0, len(just_values), 1):
            if max_value == just_values[j]:
                answer = just_keys[j] # just_values라 써서 한참 고민ㅡㅡ
                break
    else:
        answer = -1
    return answer
