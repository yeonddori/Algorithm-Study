def solution(s):
    answer = 0
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, len(eng), 1):
        if eng[i] in s:
            s = s.replace(eng[i], str(num[i]))
    s = int(s)
    return s