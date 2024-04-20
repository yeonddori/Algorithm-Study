def judge(lst):
    # set으로 각 char들 하나씩만 집합으로 표현하기
    hi = set(lst)
    temp = lst[0]

    for i in range(len(lst)):

        # 같은 문자가 쭉 나오다가, 다른문자 나오면 집합에서 '다른문자 나오기 전의 문자' 지우기
        if lst[i] != temp:
            temp = lst[i]
            hi.remove(lst[i-1])

        # 집합에 없는게 나오면 0리턴. -> 같은게 또 나왔다는 뜻임.
        if lst[i] not in hi:
            return 0

    # 마지막 잎새마냥 혼자 문자 하나만 남았음 -> 같은게 또 나오지 x
    if(len(hi)==1):
        return 1



def main():
    N = int(input())
    result = 0

    for _ in range(N):
        Str = list(input())
        result += judge((Str))

    print(result)

main()