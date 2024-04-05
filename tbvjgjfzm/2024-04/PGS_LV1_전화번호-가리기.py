def solution(phone_number):
    star_number = phone_number[0:len(phone_number) - 4]
    number = phone_number[len(phone_number) - 4:len(phone_number)]
    star = "*"*len(star_number)
    answer = star + number
    
    return answer