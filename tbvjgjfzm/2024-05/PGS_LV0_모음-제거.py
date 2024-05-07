def solution(my_string):
    tf = 0
    answer = ''
    aeiou = ['a', 'e', 'i', 'o', 'u']
    for i in range(0, len(my_string), 1):
        print(i)
        for j in range(0, len(aeiou), 1):
            if my_string[i] == aeiou[j]:
                tf = 1
        if tf == 0:
            answer = answer + my_string[i]
        tf = 0 # 한 탭 차이로 결과가 달라짐.
    return answer