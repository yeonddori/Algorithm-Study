def judge(lst):
    # set���� �� char�� �ϳ����� �������� ǥ���ϱ�
    hi = set(lst)
    temp = lst[0]

    for i in range(len(lst)):

        # ���� ���ڰ� �� �����ٰ�, �ٸ����� ������ ���տ��� '�ٸ����� ������ ���� ����' �����
        if lst[i] != temp:
            temp = lst[i]
            hi.remove(lst[i-1])

        # ���տ� ���°� ������ 0����. -> ������ �� ���Դٴ� ����.
        if lst[i] not in hi:
            return 0

    # ������ �ٻ����� ȥ�� ���� �ϳ��� ������ -> ������ �� ������ x
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