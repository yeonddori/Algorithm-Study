def solution(s, n):
    answer = ''
    for i in range(0, len(s)):
        if ord(s[i]) >= 64 and ord(s[i]) <= 90: 
            print(type(s[i]))
            Cae = ord(s[i]) + n
            if Cae > 90:
                Cae = Cae - 26
            answer = answer + chr(Cae)
        elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            Cae = ord(s[i]) + n
            print(type(Cae))
            if Cae > 122:
                Cae = Cae - 26
            answer = answer + chr(Cae)
        else:
            answer = answer + " "
    return answer