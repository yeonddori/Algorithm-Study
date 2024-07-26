def solution(a, b):
    answer = ''
    list_d = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = a - 1
    if month < 7:
        if month == 1:
            date =  31 + b - 1
        elif month == 0:
            date = b - 1
        elif month != 1 and month % 2 == 1:
            date = 31 * month - month // 2 + b - 2
        else:
            date = 61 * (month // 2) + b - 2
    elif month >= 7:
        if month % 2 == 1:
            date = 31 * month - month // 2 + b - 2
        else:
            date = 61 * (month // 2) + b - 1
    answer = list_d[date % 7]
    return answer
