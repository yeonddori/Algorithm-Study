def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            answer = True
        else:
            answer = False
    else:
        answer = False      
    return answer